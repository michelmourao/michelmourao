from fastapi import APIRouter, Depends, HTTPException, status, Body
from app.auth import oauth2_scheme
from app.utils import token_verification
from app.models import AgentModel
from app.database import session

SystemPromptsCRUD = AgentModel.SystemPromptsCRUD
SystemPromptsResponse = AgentModel.SystemPromptsResponse
SystemPromptsCreate = AgentModel.SystemPromptsCreate
SystemPromptsUpdate = AgentModel.SystemPromptsUpdate

router = APIRouter()

async def get_prompts_endpoint(prompt_id: int, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    prompt_crud = SystemPromptsCRUD(session)
    prompt = prompt_crud.read_prompt(prompt_id=prompt_id)
    session.close()

    if prompt is not None:
        print(f"Prompt encontrado: {prompt.name}")
        return prompt
    else:
        print("Prompt não encontrado")
        raise HTTPException(status_code=404, detail="Prompt not found")


@router.get("/{prompt_id}", response_model=SystemPromptsResponse)

async def read_prompts(prompt = Depends(get_prompts_endpoint)):
    return prompt


@router.post("/", response_model=SystemPromptsResponse, status_code=status.HTTP_201_CREATED)

async def create_prompt(prompt: SystemPromptsCreate = Body(...), token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    # Verifica se name está em uso
    existing_promp = SystemPromptsCRUD(session).read_prompt(name=prompt.name)
    if existing_promp:
        session.close()
        raise HTTPException(status_code=400, detail="PromptName already registered, choose another one")
    
    new_prompt = SystemPromptsCRUD(session).create_prompt(name=prompt.name, prompt=prompt.prompt)
    
    prompt_data = {
        "id": new_prompt.id,
        "name": new_prompt.name,
        "prompt": new_prompt.prompt,
    }
    
    session.close()
    
    print('New prompt created!')

    return prompt_data

@router.delete("/{prompt_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_prompt(prompt_id: int, token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception

    #verifica se o prompt existe
    existing_prompt = AgentModel.SystemPromptsCRUD(session).read_prompt(prompt_id=prompt_id)
    print(existing_prompt)

    if existing_prompt == None:
        session.close()
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    prompt_deleted = AgentModel.SystemPromptsCRUD(session).delete_prompt(prompt_id)
    session.close()
    print("Deleted: ", prompt_deleted)
    
    return

@router.put("/{prompt_id}", status_code=status.HTTP_204_NO_CONTENT)

async def update_prompt(prompt: SystemPromptsUpdate = Body(...), token: str = Depends(oauth2_scheme)):    
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    prompt_crud = AgentModel.SystemPromptsCRUD(session)

    #verifica se o novo nome está em uso, caso tenha na requisição
    if prompt.name:
        print("Checando se o novo nome existe...")
        existing_name = prompt_crud.read_prompt(name=prompt.name)
        print(existing_name)

        if existing_name == None:
            print("Nome não existe...")
            session.close()
        else:
            raise HTTPException(status_code=404, detail="The name already exists, choose another one.")

    #verifica se o prompt existe
    existing_prompt = prompt_crud.read_prompt(prompt_id=prompt.id)
    print(existing_prompt)

    if existing_prompt == None:
        session.close()
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    if prompt.name and prompt.prompt:
        print("Alterar tudo")  
        prompt_crud.update_prompt(prompt_id=prompt.id, new_name=prompt.name, new_prompt=prompt.prompt)
        
    else:
        if prompt.prompt:
            print("alterar prompt")
            prompt_crud.update_prompt(prompt_id=prompt.id, new_prompt=prompt.prompt)

        if prompt.name:
            print("Alterar nome")
            prompt_crud.update_prompt(prompt_id=prompt.id, new_name=prompt.name)

    return prompt