from datetime import datetime
import typing
from pydantic import BaseModel, Field, field_validator, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(le=20, ge=1)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: typing.Optional[str] = None

    @field_validator("notes")
    def check_notes(cls, value):
        if len(value) > 200:
            raise ValueError("Note is too long")
        return (value)


def main():
    print("Space Station Data \
Validation\n========================================")
    try:
        station = SpaceStation(station_id="512",
                               name="test", crew_size=10, power_level=20.0,
                               oxygen_level=20.0,
                               last_maintenance=datetime.now())
        print("Valid station created:")
        print("ID:", station.station_id)
        print("Name:", station.name)
        print("Crew:", station.crew_size, "people")
        print("Power:", station.power_level, "%")
        print("Oxygen:", station.oxygen_level, "%")
        if (station.is_operational is True):
            print("Status: Operational")
        else:
            print("Status: In need of maintenance\n")
    except ValidationError as obj:
        print("Excepted validation error:")
        print("", obj.errors()[0]['msg'])
    try:
        station = SpaceStation(station_id="512", name="test",
                               crew_size=30, power_level=20.0,
                               oxygen_level=20.0,
                               last_maintenance=datetime.now())
        print("Valid station created:")
        print("ID:", station.station_id)
        print("Name:", station.name)
        print("Crew:", station.crew_size, "people")
        print("Power:", station.power_level, "%")
        print("Oxygen:", station.oxygen_level, "%")
        if (station.is_operational is True):
            print("Status: Operational")
        else:
            print("Status: In need of maintenance\n")
    except ValidationError as obj:
        print("Found validation error:")
        print(f" {obj.errors()[0]['loc'][0]}: {obj.errors()[0]['msg']}")


if __name__ == "__main__":
    main()
