import glob


extentions = "csv"

p = glob.glob(f"**/*.{extentions}",recursive=True)

print("\n".join(i for i in p))
