from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from datetime import datetime

# Asegúrate de importar get_db desde tu archivo de base de datos real
from database import get_db
from models.inventario import InventarioModel
from schemas.inventario import InventarioCreate, InventarioUpdate, InventarioResponse

router = APIRouter(
    prefix="/api/v1/inventario",
    tags=["Inventario y Lotes Agrícolas"]
)

@router.get("", response_model=List[InventarioResponse])
def listar_inventario(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    elementos = db.query(InventarioModel).offset(skip).limit(limit).all()
    return elementos

@router.post("", response_model=InventarioResponse, status_code=status.HTTP_201_CREATED)
def crear_inventario(item: InventarioCreate, db: Session = Depends(get_db)):
    estado_cultivo = item.estado_cultivo if item.tipo == "lote_cultivo" else None
    cantidad = item.cantidad if item.tipo == "insumo" else None
    unidad_medida = item.unidad_medida if item.tipo == "insumo" else None

    nuevo_item = InventarioModel(
        nombre=item.nombre,
        tipo=item.tipo,
        area_m2=item.area_m2,
        estado_cultivo=estado_cultivo,
        cantidad=cantidad,
        unidad_medida=unidad_medida,
        descripcion=item.descripcion,
        fecha_registro=datetime.utcnow()
    )
    
    db.add(nuevo_item)
    db.commit()
    db.refresh(nuevo_item)
    return nuevo_item

@router.put("/{id}", response_model=InventarioResponse)
def actualizar_inventario(id: int, item_update: InventarioUpdate, db: Session = Depends(get_db)):
    item = db.query(InventarioModel).filter(InventarioModel.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    
    # Extraemos solo los campos que el cliente decidió actualizar
    datos_actualizacion = item_update.dict(exclude_unset=True)
    
    for key, value in datos_actualizacion.items():
        # Validamos reglas de negocio según el tipo de elemento
        if key == "estado_cultivo" and item.tipo != "lote_cultivo":
            continue  
        if key == "cantidad" and item.tipo != "insumo":
            continue  
        setattr(item, key, value)
        
    db.commit()
    db.refresh(item)
    return item