from datetime import datetime
import typing
from enum import Enum
from pydantic import BaseModel, Field, \
    field_validator, ValidationError, model_validator


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: typing.Optional[str] = None
    is_verified: bool = Field(default=False)

    @field_validator("message_received")
    def check_message(cls, value):
        if len(value) > 500:
            raise Exception("Message received is too long")
        return (value)

    @model_validator(mode='after')
    def check_id(self):
        if self.contact_id[0] != "A" or self.contact_id[1] != "C":
            raise Exception('Wrong ID, must start by AC')
        return self

    @model_validator(mode='after')
    def check_physical(self):
        if self.contact_type.name == "physical" and self.is_verified is False:
            raise Exception('Physical contacts must be verified')
        return self

    @model_validator(mode='after')
    def check_telepathic(self):
        if self.contact_type.name == "telepathic" and self.witness_count < 3:
            raise Exception('Telepathic contacts \
must have at least 3 witnesses')
        return self

    @model_validator(mode='after')
    def check_signal(self):
        if self.signal_strength >= 7.0 and self.message_received is None:
            raise Exception('Strong signals must have their messages recorded')
        return self


def print_contact(contact: AlienContact):
    try:
        print("Valid Contact Log:")
        print("ID:", contact.contact_id)
        print("Name:", contact.contact_type)
        print("Location:", contact.location, "people")
        print("Signal:", contact.signal_strength, "/ 10")
        print("Duration:", contact.duration_minutes, "minutes")
        print("Witnesses:", contact.witness_count)
        if (contact.message_received is None):
            print("No message has been deciphered")
        else:
            print("Message:", contact.message_received)
        if (contact.is_verified is True):
            print("Contact has been verified\n")
        else:
            print("Contact has not been verified\n")
    except ValidationError as obj:
        print("Found validation error:")
        print(f" {obj.errors()[0]['loc'][0]}: {obj.errors()[0]['msg']}\n")


def main():
    print("Alien Contact Log \
Validation\n======================================")
    try:
        contact1 = AlienContact(
            contact_id="AC145",
            timestamp=datetime.now(),
            location="New York",
            contact_type=ContactType.radio,
            signal_strength=6.0,
            duration_minutes=80,
            witness_count=3,
        )
        print_contact(contact1)
    except Exception as obj:
        print("Found invalid model:\n", obj, "\n")
    print("======================================")
    try:
        contact2 = AlienContact(
            contact_id="AC145",
            timestamp=datetime.now(),
            location="New York",
            contact_type=ContactType.radio,
            signal_strength=6.0,
            duration_minutes=80,
            witness_count=3,
            message_received="ddddddddd\
ddddddddddddddddddddddddddddddddddddddddd\
dddddddddddddddddddddddddddddddddddddddddddd\
ddddddddddddddddddddddddddddddddddddddddddddd\
ddddddddddddddddddddddddddddddddddddddddddddd\
ddddddddddddddddddddddddddddddddddddddddddddd\
dddddddddddddddddddddddddddddddddddddddddddddd\
dddddddddddddddddddddddddddddddddddddddddddddd\
ddddddddddddddddddddddddddddddddddddddddddddddd\
dddddddddddddddddddddddddddddddddddddddddddddddd\
ddddddddddddddddddddddddddddddddddddddddddddddd\
ddddddddddddddddddddddddddddddddddddddddddddddd\
ddddddddddddddddddddddddddddddddddddddddddddddd\
dddddddddddddddddddddddddddddddddddd"
        )
        print_contact(contact2)
    except Exception as obj:
        print("Found invalid model:\n", obj, "\n")
    print("======================================")
    try:
        contact3 = AlienContact(
            contact_id="AC145",
            timestamp=datetime.now(),
            location="New York",
            contact_type=ContactType.radio,
            signal_strength=7.0,
            duration_minutes=80,
            witness_count=3,
        )
        print_contact(contact3)
    except Exception as obj:
        print("Found invalid model:\n", obj, "\n")
    print("======================================")
    try:
        contact4 = AlienContact(
            contact_id="A14dd5",
            timestamp=datetime.now(),
            location="New York",
            contact_type=ContactType.radio,
            signal_strength=7.0,
            duration_minutes=80,
            witness_count=3,
        )
        print_contact(contact4)
    except Exception as obj:
        print("Found invalid model:\n", obj, "\n")
    print("======================================")
    try:
        contact5 = AlienContact(
            contact_id="AC4dd5",
            timestamp=datetime.now(),
            location="New York",
            contact_type=ContactType.physical,
            signal_strength=7.0,
            duration_minutes=80,
            witness_count=3,
        )
        print_contact(contact5)
    except Exception as obj:
        print("Found invalid model:\n", obj, "\n")
    print("======================================")
    try:
        contact6 = AlienContact(
            contact_id="AC4dd5",
            timestamp=datetime.now(),
            location="New York",
            contact_type=ContactType.telepathic,
            signal_strength=7.0,
            duration_minutes=80,
            witness_count=2,
        )
        print_contact(contact6)
    except Exception as obj:
        print("Found invalid model:\n", obj)


if __name__ == "__main__":
    main()
