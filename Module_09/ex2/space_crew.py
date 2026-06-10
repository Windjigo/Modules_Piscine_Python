from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, model_validator


class Rank(Enum):
    cadet = 1
    officer = 2
    lieutenant = 3
    captain = 4
    commander = 5


class Crewmember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[Crewmember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_id(self):
        if self.mission_id[0] != "M":
            raise Exception('All missions IDs must start with M')
        return self

    @model_validator(mode='after')
    def check_rank(self):
        i = 0
        for x in self.crew:
            if (x.rank == Rank.commander or x.rank == Rank.captain):
                i += 1
        if (i == 0):
            raise Exception("All missions \
must have at least one high-ranking crewmember")
        return self

    @model_validator(mode='after')
    def check_length(self):
        i = 0
        for x in self.crew:
            if (x.years_experience >= 5):
                i += 1
        if self.duration_days > 365 and i < len(self.crew)/2:
            raise Exception("Long missions \
must have at least 50% experienced crewmates")
        return self

    @model_validator(mode='after')
    def check_activity(self):
        for x in self.crew:
            if (x.is_active is False):
                raise Exception("All crewmates must currently be active")
        return self


def print_model(model: SpaceMission):
    print("Valid mission created:")
    print("Mission:", model.mission_name)
    print("ID:", model.mission_id)
    print("Destination:", model.destination)
    print("Duration:", model.duration_days, "days")
    print("Budget:", model.budget_millions, "M")
    print("Crew size:", len(model.crew))
    print("Crew members:")
    for i in model.crew:
        print("-", i.name, f"({i.rank.name}) - {i.specialization}")
    print("")


def main():
    crew1 = Crewmember(
        member_id="alpha",
        name="Sarah Connor",
        rank=Rank.commander,
        age=28,
        specialization="Mission command",
        years_experience=10,
    )
    crew2 = Crewmember(
        member_id="beta",
        name="John Smith",
        rank=Rank.lieutenant,
        age=25,
        specialization="Navigation",
        years_experience=5,
    )
    crew3 = Crewmember(
        member_id="gamma",
        name="Alice Johnson",
        rank=Rank.officer,
        age=22,
        specialization="Engineering",
        years_experience=3,
    )
    crew4 = Crewmember(
        member_id="delta",
        name="Remi Ratatouile",
        rank=Rank.cadet,
        age=18,
        specialization="Stagiaire",
        years_experience=0,
    )
    crew5 = Crewmember(
        member_id="omega",
        name="Surprise Attack",
        rank=Rank.commander,
        age=80,
        specialization="Surprise Attack",
        years_experience=50,
        is_active=False,
    )
    print("Space Mission Crew \
Validation\n======================================")
    try:
        contact1 = SpaceMission(
            mission_id="M00314",
            mission_name="Moon landing",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=60,
            crew=[crew1, crew2, crew3],
            budget_millions=400.5,
        )
        print_model(contact1)
    except Exception as obj:
        print("Found invalid mission:\n", obj, "\n")
    print("======================================")
    try:
        contact2 = SpaceMission(
            mission_id="00314",
            mission_name="Moon landing",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=60,
            crew=[crew1, crew2, crew3],
            budget_millions=400.5
        )
        print_model(contact2)
    except Exception as obj:
        print("Found invalid mission:\n", obj, "\n")
    print("======================================")
    try:
        contact4 = SpaceMission(
            mission_id="M00314",
            mission_name="Moon landing",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=60,
            crew=[crew2, crew3],
            budget_millions=400.5
        )
        print_model(contact4)
    except Exception as obj:
        print("Found invalid mission:\n", obj, "\n")
    print("======================================")
    try:
        contact5 = SpaceMission(
            mission_id="M00314",
            mission_name="Moon landing",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=366,
            crew=[crew1, crew3, crew4],
            budget_millions=400.5
        )
        print_model(contact5)
    except Exception as obj:
        print("Found invalid mission:\n", obj, "\n")
    print("======================================")
    try:
        contact6 = SpaceMission(
            mission_id="M00314",
            mission_name="Moon landing",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=60,
            crew=[crew5, crew2, crew3],
            budget_millions=400.5
        )
        print_model(contact6)
    except Exception as obj:
        print("Found invalid mission:\n", obj)


if __name__ == "__main__":
    main()
