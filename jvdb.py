import asyncio
from motor import motor_asyncio

class MongoDB:
    def __init__(self, url: str):
        self.client = motor_asyncio.AsyncIOMotorClient(url)
        self.db = self.client.giveawaybot  # The database "giveawaybot"
        self.mygiveaways = self.db.mygiveaways  # The collection "mygiveaways"
    
    # Create or get a user's database collection (userId)
    async def add_giveawayid(self, userid: int):
        # Check if the user already has a collection
        if not (await self.mygiveaways.find_one({"_id": userid})):
            await self.mygiveaways.insert_one({"_id": userid})  # Create an entry for the user
            return self.db[str(userid)]  # Dynamically create a collection for the user
        else:
            return None
    
    # Add giveaway information to a user's collection
    async def add_giveaway(self, userid: int, winners: int, msg_text: str, giveaway_text: str):
        userDb = await self.add_giveawayid(userid)
        if userDb:
            # Insert giveaway data for the user
            await userDb.insert_one({
                "_id": "data", "winners": winners, "msg_text": msg_text, "giveaway_text": giveaway_text
            })
            return True
        return False

# Main function to execute
async def main():
    try:
        # Replace with your MongoDB Atlas connection string
        db = MongoDB('mongodb+srv://kalawativerma80:CUhwW7zAu2RA900S@cluster0.vxnio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        # Add giveaway data for a user (userId=12345, winners=3, and sample messages)
        result = await db.add_giveaway(12345, 3, "Win a prize!", "React with ❤️ to participate!")
        if result:
            print("Giveaway data added successfully!")
        else:
            print("Error adding giveaway data.")
    except Exception as e:
        print(f"Error: {e}")

# Run the asynchronous main function
asyncio.run(main())
