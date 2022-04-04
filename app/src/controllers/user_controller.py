from fastapi import APIRouter, Response, status, HTTPException
from configurations.injection import UserInjection
from domains.user_role import UserRole

router = APIRouter(prefix='/user')