import sys
print(sys.argv)

if len(sys.argv) < 3:

	print("Usage: python3 deploy.py <app> <environment>")
else:
	app = sys.argv[1]
	env = sys.argv[2]
	print(f"Deploying {app} to {env}")
