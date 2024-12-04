import sqlite3

connection_string = sqlite3.connect("./database/videos.db")

cursor = connection_string.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        duration TEXT NOT NULL
    )
""")


def load_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    print("RAW Data: ", videos)


    print("\n")
    print("*" * 20)

    if len(videos) == 0:
        print("No videos found")

        print("*" * 20)
        print("\n")
        return
    else:
        for row in videos:
            print(f"ID: {row[0]}, Name: {row[1]}, Duration: {row[2]}")

    print("*" * 20)
    print("\n")




def add_new_video(name, duration):
    if name == "" or duration == "":
        print("Name and duration cannot be empty")
        return
    
    cursor.execute("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))

    connection_string.commit()



def update_video(video_ID, name, duration):
    
    existing_video_name = cursor.execute("SELECT name FROM videos WHERE id = ?", (video_ID,)).fetchone()

    existing_video_duration = cursor.execute("SELECT duration FROM videos WHERE id = ?", (video_ID,)).fetchone()

    if name == "":
        name = existing_video_name[0]

    if duration == "":
        duration = existing_video_duration[0]


    cursor.execute("UPDATE videos SET name = ?, duration = ? WHERE id = ?", (name, duration, video_ID))

    connection_string.commit()



def delete_video(video_ID):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_ID,))

    connection_string.commit()




def main():
    while True:
        print("\n Youtube Manager App Powerd by SQLite3 \n")
        print("1. Press 1 to view all videos")
        print("2. Press 2 to add a new video")
        print("3. Press 3 to update a video details")
        print("4. Press 4 to delete a video")
        print("5. Press 5 Exit from the app\n")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                load_all_videos()

            case '2':
                video_name = input("Enter video name: ")
                video_duration = input("Enter video duration: ")
                add_new_video(video_name, video_duration)

            case '3':
                video_ID = input("Enter video ID for info updation: ")
                
                video_name = input("Enter video name: ")
                video_duration = input("Enter video duration: ")

                update_video(video_ID, video_name, video_duration)

            case '4':
                video_ID = input("Enter video ID: ")
                delete_video(video_ID)

            case '5':
                break

            case _:
                print("Invalid choice")
    
    connection_string.close()

            
if __name__ == "__main__":
    main()
