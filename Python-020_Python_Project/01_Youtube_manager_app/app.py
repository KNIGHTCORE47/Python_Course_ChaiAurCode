import json



# NOTE - Json library in python helps to create and json file types. It has major 2 methods:

# 1. dump:
# ---    Dump method helps to write data inside of a json file. It accepts 2 arguments:
# ---    First argument is the data that you want to write inside of the json file.
# ---    Second argument is the file path.

# 2. load:
# ---    Load method helps to read data inside of a json file. It accepts 1 argument:
# ---    The argument is file path.





json_data_filePath = "./json_data/videos.txt"

def load_info():
    try:
        with open(json_data_filePath, 'r') as file:
            return json.load(file)
    
    except FileNotFoundError:
        return []

def auto_save_helper(videos):
    with open(json_data_filePath, 'w') as file:
        json.dump(videos, file)     # .dump(value, file-path)




def load_all_videos(videos):
    print("\n")
    print("*" * 20)

    for index, values in enumerate(videos, start=1):
        print(f"{index}. Name: {values['name']}, Duration: {values['duration']}")

    print("*" * 20)
    print("\n")

def add_new_video(videos):
    video_name = input("Enter video name: ")
    video_duration = input("Enter video duration: ")

    videos.append({
        "name": video_name,
        "duration": video_duration
    })

    auto_save_helper(videos)

def update_video(videos):
    load_all_videos(videos)

    index_of_video = int(input("Enter video index: "))

    if 1 <= index_of_video <= len(videos):

        current_video_index = videos[index_of_video - 1]
        current_video_name = current_video_index["name"]
        current_video_duration = current_video_index["duration"]

        video_name = input("Enter video name: ")
        video_duration = input("Enter video duration: ")


        # NOTE - If the video name and video duration are empty then it will be updated with the current video name and video duration
        if video_name == "":
            video_name = current_video_name

        if video_duration == "":
            video_duration = current_video_duration
            
        # NOTE - If the video name and video duration are not empty then it will be updated with the new video name and video duration
        videos[index_of_video - 1] = {
            "name": video_name,
            "duration": video_duration
        }

        auto_save_helper(videos)

    else:
        print("Invalid index selected")

def delete_video(videos):
    load_all_videos(videos)


    index_of_video = int(input("Enter video index: "))

    if 1 <= index_of_video <= len(videos):

        del videos[index_of_video - 1]

        print("Video deleted successfully")
        
        auto_save_helper(videos)

    else:
        print("Invalid index selected")






def main():
    videos = load_info()
    while True:
        print("\n Youtube Manger App\n")
        print("1. Press 1 to view all videos")
        print("2. Press 2 to add a new video")
        print("3. Press 3 to update a video details")
        print("4. Press 4 to delete a video")
        print("5. Press 5 Exit from the app\n")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                load_all_videos(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":      # Dunder method denotes double underscore
    main()