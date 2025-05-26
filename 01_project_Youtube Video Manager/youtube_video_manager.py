import json
def load_data():
    try: 
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def data_saving_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos, file)

def list_videos(videos):
    print("x" * 30 + " Video List " + "x" * 30)
    for index, vid in enumerate(videos, start=1):
        print(f"{index}. {vid['name']}, {vid['time']}")
    print("x" * 30 + " Video List " + "x" * 30)
    

def add_video(videos):
    name = input("Enter the name of video: ")
    time = input("Enter the duration of video: ")
    videos.append({'name':name,'time':time})
    data_saving_helper(videos)

def update_video(videos):
    list_videos(videos)
    index = int(input("Enter the index of Video you want to Update: "))
    
    if 1<= index <= len(videos):
        name = input("Enter the Updated Name: ")
        time = input("Enter the Updated Time: ")
        videos[index-1] = {'name':name, 'time':time}
        data_saving_helper(videos)
    else:
        print("Invalid index")
        
def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter the index of video you want to Delete: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        data_saving_helper(videos)
        print("Video Removed Successfully")
    else:
        print("Invalid Index passed")

def main():
    videos = load_data()
    while True:
        print("\n----YOUTUBE VIDEO MANAGER---- | Choose an Option")
        print("1. List all the Videos")
        print("2. Add a Video")
        print("3. Update a Video")
        print("4. Delete a Video")
        print("5. Exit App")
        choice =  input("Enter your choice: ")
        
        match choice:
            case '1': list_videos(videos)
            case '2': add_video(videos)
            case '3': update_video(videos)
            case '4': delete_video(videos)
            case '5': break
            case _: print("Invalid Choice")
                
if __name__ == "__main__":
    main()