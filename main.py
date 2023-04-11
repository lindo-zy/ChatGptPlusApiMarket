#!/usr/bin/python3
# -*- coding:utf-8 -*-

from chatgpt.app import creat_app

app = creat_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app',
                host='127.0.0.1',
                port=3003,
                # debug=True,
                # reload=True
                )
