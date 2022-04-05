FROM node:17
COPY . /juice-shop
WORKDIR /juice-shop
RUN npm install
# RUN cd frontend && npm install --legacy-peer-deps && cd ..
# RUN npm run build:frontend
# RUN npm run build:server || cd .

EXPOSE 3000
CMD ["npm", "start"]