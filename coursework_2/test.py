import json
a = 'зоя изо ими имя ком мои моя око пик яиц коми копи окоп пики измок копия микоз опция покои помои'.split()
with open('test.txt', 'w', encoding='utf-8') as f:
    json.dump(a, f, ensure_ascii=False)
