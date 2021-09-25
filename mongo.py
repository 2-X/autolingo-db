from bson.objectid import ObjectId
from pymongo import MongoClient
client = MongoClient(port=27017)
db=client.autolingo


def upsert(data):
    """ upsert into MongoDB """

    # insert skill under its unique ID
    skill_data = data.get("skill", {})
    skill_id = skill_data.get("id")
    db.skills.update_one(
        {"_id": skill_id},
        {"$set": skill_data},
        upsert=True
    )

    # insert challenge under its unique ID
    challenge_data = data.get("challenge", {})
    challenge_id = challenge_data.get("id")

    # create unique challenge ID out of
    # the challenge generator ID, type of challenge, and gender of TTS
    challenge_generator_identifier = challenge_data.get("challengeGeneratorIdentifier", {})
    generator_id = challenge_generator_identifier.get("generatorId", "").lower()
    specific_type = challenge_generator_identifier.get("specificType", "").lower()
    character_gender = challenge_data.get("character", {}).get("gender", "").lower()
    challenge_id = f"{generator_id}-{specific_type}-{character_gender}"

    # link to skill ID
    challenge_data["skill_id"] = skill_id

    # upsert
    db.challenges.update_one(
        {"_id": challenge_id},
        {"$set": challenge_data},
        upsert=True
    )
