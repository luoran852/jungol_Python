git config --global user.email hannn0414@naver.com
git config --global user.name luoran852

# 초기 생성 
git init

git add .
git commit -m "first commit"

git remote add origin https://github.com/luoran852/jungol_Python.git

git push -u origin master

# 이후 업데이트
git add .
git commit -m "xxx commit"
git push

# 저장소 -> 로컬
git pull