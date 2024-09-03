import sys,os 
import uvicorn
sys.path.append(os.getcwd())
from fastapi import FastAPI
from src.routers import router
from fastapi.openapi.utils import get_openapi app FastAPI()
def custom_openapi():
if app.openapi_schema:
return app.openapi_schema
openapi_schema = get_openapi(
openapi_version="2.0",
title="SH CV Matcher APIs",
version="1.0",
description="REST APIs for SH CV Matcher", routes=app.routes
)
openapi_schema ["components"] = {}
openapi_schema ["components"]["securitySchemes"] = {
"bearerAuth": {
}
"type": "http",
"scheme": "bearer",
"bearerFormat": "JWT",
}
openapi_schema ["components"]["security"] = [{"bearerAuth": []}]
openapi_schema ["security"] = [{"bearerAuth": []}]
openapi_schema ["servers"] = [{"url": "https://apis.simplihire.ai"}]
app.openapi_schema = openapi_schema
return app.openapi_schema
app.openapi =
custom_openapi
@app.get("/cv-matcher-api/openapi.json", include_in_schema=False)
async def get_openapi_endpoint():
openapi_schema = custom_openapi()
return openapi_schema
app.include_router (router.api_router)
