

rm -rf project
rm -rf restored_project
rm -f project.tar.gz

mkdir -p project/src project/docs project/scripts project/backup

touch project/src/main.py
touch project/docs/user_guide.txt
touch project/scripts/install.sh

cp project/src/main.py project/backup/main.py.bak
mv project/docs/user_guide.txt project/docs/application_guide.txt

find project -name "*.py"

chmod 755 project/scripts/install.sh

tar -czf project.tar.gz project

mkdir -p restored_project
tar -xzf project.tar.gz -C restored_project

ls -R restored_project
