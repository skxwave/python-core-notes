from datetime import datetime

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from src.schemas.notes import CreateNote, Note
from src.core.auth.transport import current_active_user

router = APIRouter(
    tags=["Notes"],
    dependencies=[Depends(current_active_user)],
)
notes: list[Note] = []


async def get_note_by_id(note_id: int):
    """Retrieves the note by its ID"""
    for note in notes:
        if note.id == note_id:
            return note

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Note not found",
    )


@router.get(
    "/",
    response_model=list[Note],
    status_code=status.HTTP_200_OK,
)
async def get_all_notes() -> list[Note]:
    """Retrieves the list of notes"""
    return notes


@router.get(
    "/{note_id}",
    response_model=Note,
    status_code=status.HTTP_200_OK,
)
async def get_note(note: Note = Depends(get_note_by_id)):
    """Retrieves the note by its ID"""
    return note


@router.post(
    "/",
    response_model=Note,
    status_code=status.HTTP_201_CREATED,
)
async def create_note(note: CreateNote):
    """Create note"""
    new_id = len(notes) + 1

    data = Note(
        id=new_id,
        title=note.title,
        text=note.text,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    notes.append(data)

    return data
