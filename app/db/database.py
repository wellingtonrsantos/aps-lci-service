import json
from pathlib import Path
from sqlmodel import SQLModel, create_engine, Session, select
from app.models.lci_models import LCIProduct, LCIFlow

DATABASE_URL = "sqlite:///lci.db"
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        exists = session.exec(select(LCIProduct)).first()
        if exists:
            return

        seed_file = Path("data/seed_lci.json")
        if not seed_file.exists():
            print("Arquivo de seed não encontrado.")

        with seed_file.open("r", encoding="utf-8") as f:
            products = json.load(f)

        for product_data in products:
            product = LCIProduct(
                name=product_data["name"], description=product_data.get("description")
            )
            session.add(product)
            session.commit()
            session.refresh(product)

            flows = [
                LCIFlow(product_id=product.id, **flow_data)
                for flow_data in product_data["flows"]
            ]
            session.add_all(flows)

        session.commit()
        print("Base LCI populada com dados iniciais.")
