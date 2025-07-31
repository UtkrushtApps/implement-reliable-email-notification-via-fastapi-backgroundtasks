from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import UserUpdate, UserOut
from app.database import get_async_session

router = APIRouter(prefix="/users", tags=["users"])

@router.put("/{user_id}", response_model=UserOut)
async def update_user_profile(
    user_id: int,
    user_update: UserUpdate,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_async_session)
):
    # Update the user profile in the database (logic not implemented)
    # Trigger background email notification here
    pass
