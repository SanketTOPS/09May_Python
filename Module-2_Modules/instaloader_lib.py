import instaloader


insta_id=input("Enter your Instagram ID:")

insta=instaloader.Instaloader()

insta.download_profile(insta_id)

print("Profile downloaded successfully!")