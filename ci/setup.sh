virtualenv --python=/usr/bin/python3 env &&\
cd env/bin &&\
source activate &&\
cd ../.. &&\
pip3 install -r ./requirements.txt