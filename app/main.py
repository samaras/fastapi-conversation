import fastapi
import uvicorn

from db.database import SessionLocal, engine
from api.campaign import router as campaign_router
from api.customer import router as customer_router
from api.deal import router as deal_router
from api.email import router as email_router
from api.lead import router as lead_router
from api.user import router as user_router


app = fastapi.FastAPI()

app.include_router(campaign_router)
app.include_router(customer_router)
app.include_router(deal_router)
app.include_router(lead_router)
app.include_router(email_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8081, host="127.0.0.1", reload=True)
