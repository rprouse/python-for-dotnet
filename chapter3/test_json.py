import json
import typing

def main() -> None:
    with open('/Src/Reliq/aws-cli-s3-deploy/env_jsons/Anglicare.json') as json_file:
        env_json = json.load(json_file)

    env_json.pop('envs', None)
    print(json.dumps(env_json, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()