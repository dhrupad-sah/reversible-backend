from fastapi import APIRouter, HTTPException
from ..db.supabase import supabase_client

router = APIRouter(
    prefix="/users",
    tags=["users"]
)
@router.get("/get-user-balance/{wallet_address}")
async def get_user_balance(wallet_address: str):
    try:
        user_balance = supabase_client.table("users").select("*").eq("wallet_address", wallet_address).execute()
        return {"status": "success", "data": user_balance.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/get-user-transactions/{wallet_address}")
async def get_user_transactions(wallet_address: str):
    try:
        user_transactions = supabase_client.table("transactions").select("*").eq("wallet_address", wallet_address).execute()
        return {"status": "success", "data": user_transactions.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
