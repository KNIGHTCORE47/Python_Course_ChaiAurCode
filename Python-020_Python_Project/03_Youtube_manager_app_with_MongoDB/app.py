import pymongo
from dotenv import dotenv_values
from constants import DB_NAME
from bson import ObjectId

def db_connection():
    config = dotenv_values(".env")

    try:
        connection_string = f"{config["MONGODB_URI"]}/"

        client = pymongo.MongoClient(connection_string, tlsAllowInvalidCertificates=True)

        #NOTE - tlsAllowInvalidCertificates=True is not a good way to add SSL certificates.

        db = client[DB_NAME]

        video_collection = db["videos"]

        return video_collection
    except Exception as e:
        print(e)


def load_all_videos():
    video_collection = db_connection()

    list_of_videos = video_collection.find({})  

    # NOTE - Here video_collection.find({}) is a iteratable object

    # print("RAW Data: ", list_of_videos)
    # print(type(list_of_videos)) # Output: <class 'pymongo.cursor.Cursor'>

    print("\n")
    print("*" * 20)

    if not list(list_of_videos):
        print("No videos found")

        print("*" * 20)
        print("\n")
        return

    for video in video_collection.find({}):

        print(f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['duration']}")

    print("*" * 20)
    print("\n")


def add_new_video(video_name, video_duration):
    video_collection = db_connection()

    video_collection.insert_one(
        {
            "name": video_name,
            "duration": video_duration
        }
    )


def update_video(video_ID, video_name, video_duration):
    video_collection = db_connection()

    result = video_collection.find_one(
        {"_id": ObjectId(video_ID)}
    )

    # print(result)

    if not result:
        print("Video not found")
        return
    
    if video_name == "":
        video_name = result["name"]

    if video_duration == "":
        video_duration = result["duration"]


    video_collection.update_one(
        {"_id": ObjectId(video_ID)},
        {
            "$set": {
                "name": video_name,
                "duration": video_duration
            }
        }
    )


def delete_video(video_ID):
    video_collection = db_connection()

    video_collection.delete_one(
        {"_id": ObjectId(video_ID)}
        )





def main():
    while True:
        print("\n Youtube Manager App Powerd by MongoDB \n")
        print("1. Press 1 to view all videos")
        print("2. Press 2 to add a new video")
        print("3. Press 3 to update a video details")
        print("4. Press 4 to delete a video")
        print("5. Press 5 Exit from the app\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            load_all_videos()

        elif choice == '2':
            video_name = input("Enter video name: ")
            video_duration = input("Enter video duration: ")
            add_new_video(video_name, video_duration)

        elif choice == '3':
            video_ID = input("Enter video ID for info updation: ")

            video_name = input("Enter video name: ")
            video_duration = input("Enter video duration: ")
            update_video(video_ID, video_name, video_duration)

        elif choice == '4':
            video_ID = input("Enter video ID: ")
            delete_video(video_ID)

        elif choice == '5':
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()