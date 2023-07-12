# SSAFY, REACT 모듈형 특강



### 0705

```bash
$ npm install -g pnpm
```

```bash
# typescript 서버 실
$ pnpm add -D live-server typescript
```



```json
{
  "type": "module",
  "scripts": {
    "dev": "pnpm watch | pnpm serve",
    "serve": "live-server --host=localhost --port=3000 --no-browser",
    "compile": "tsc -p tsconfig.json",
    "watch": "pnpm compile --watch"
  },
  "devDependencies": {
    "live-server": "1.2.2",
    "ts-node": "10.9.1",
    "typescript": "5.1.6"
  }
}
```

```bash
# 서버 실행  
pnpm serve

#
pnpm tsc --init
```



- react 는 v-for 가 존재하지 않으니 map 을 잘 알아둬야함!
