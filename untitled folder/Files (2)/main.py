import subprocess

# Fetch the list of repositories from the artifact registry
def get_repositories():
    command = "gcloud artifacts repositories list --format='table(name,LOCATION)' | tail -n +2"
    result = subprocess.check_output(command, shell=True).decode('utf-8')
    
    # Parse the result into an array of tuples (name, location)
    repos = [tuple(line.split()) for line in result.strip().split('\n')]
    print(repos)
    return repos

# Set cleanup policies for each repository
def set_cleanup_policies(repos):
    for repo, location in repos:
        policy_path = "artifact-deletion-policy.json"
        command = f"gcloud artifacts repositories set-cleanup-policies {repo} --location {location} --policy={policy_path} --no-dry-run"
        
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Successfully set cleanup policy for {repo} in {location}")
        except subprocess.CalledProcessError as e:
            print(f"Error setting cleanup policy for {repo}: {e}")

# Main execution
def main():
  
  repositories = get_repositories()
  set_cleanup_policies(repositories)

if __name__ == "__main__":
    main()
