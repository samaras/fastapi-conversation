from sendgrid import SendGridAPIClient, TwilioEmailAPIClient
from sendgrid.helpers.mail import Mail

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.email import Email
from schemas.email import EmailCreate
from settings import settings

TWILIO_ACCOUNT_SID = settings.twilio_account_sid 
TWILIO_AUTH_TOKEN = settings.twilio_auth_token


class EmailService:
    @staticmethod
    def send_email(api_key: str, email_data: EmailCreate, db: Session):
        sg = SendGridAPIClient(api_key)
        twilio_email = TwilioEmailAPIClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = Mail(
            from_email=email_data.sender,
            to_emails=email_data.recipient,
            subject=email_data.subject,
            plain_text_content=email_data.body,
            html_content=email_data.body,
        )

        # message.tracking_settings = {"open_tracking": {"enable": True}}

        try:
            response = sg.send(message)
            if response.status_code == 202:
                email_id = response.headers.get("X-Message-Id")
                email_data.sendgrid_email_id = email_id
                email_model = Email(**email_data.dict())
                db.add(email_model)
                db.commit()
                db.refresh(email_model)

                return email_model
            else:
                raise HTTPException(
                    status_code=response.status_code, detail="Failed to send email"
                )
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error sending email: {str(e)}"
            )

    @staticmethod
    def track_email_open(sendgrid_email_id: str, db: Session):
        sg = SendGridAPIClient(api_key=settings.sendgrid_api_key)

        is_opened = False
        try:
            response = sg.client.campaigns.stats.get(
                query_params={"id": sendgrid_email_id}
            )
            if response.status_code == 200:
                data = response.body
                # Check if the email has been opened, blocks will be empty if email opened
                if data.get("stats"):
                    if not data["stats"].get("blocks"):
                        is_opened = True
                else:
                    print(
                        f"Failed to get email stats. Status Code: {response.status_code}"
                    )

        except Exception as e:
            print(f"An error occured: {e}")
            is_opened = False

        email = (
            db.query(Email).filter(Email.sendgrid_email_id == sendgrid_email_id).first()
        )

        if is_opened:
            email.is_opened = True
            db.commit()

    @staticmethod
    def get_email_open_status(email_id: int, db: Session):
        email = db.query(Email).filter(Email.id == email_id).first()

        if email:
            return {"email_id": email_id, "is_opened": email.is_opened}
        else:
            raise HTTPException(status_code=404, detail="Email not found")
