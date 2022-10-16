import glob


extentions = "csv" # change it to anything you need to find

p = glob.glob(f"**/*.{extentions}",recursive=True)

print("\n".join(i for i in p))
