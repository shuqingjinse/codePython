# 问题三的源代码
import random
def generate():
    simple_grammar = """
    sentence => noun_phrase verb_phrase preposition
    noun_phrase => Article Adj* noun
    Adj* => null | Adj Adj*
    verb_phrase => verb noun_phrase
    Article => 一个 | 这个
    noun => 女人 | 篮球 | 桌子 | 小猫 | 男生 | 法官
    verb => 看着 | 坐在 | 听着 | 看见
    Adj => 蓝色的 | 好看的 | 小小的
    preposition => 上面 | 下面 | 中间
    """
    grammarSplit = simple_grammar.split('\n')

    dict1 = {}
    for hang in grammarSplit:
        word = hang.split(' ')
        for i in word:
            if i == '=>':
                key_list = word[word.index(i)-1]
                value_list = word[(-(len(word)-word.index(i)-1)):]
                item = {key_list : value_list}
                #print(item)
                dict1.update(item)
                break
    print('+++++++++++++++')
    listX = []
    wordPrint(dict1, 'sentence', listX)
    wordString = "".join(listX)
    print(wordString)
    print('+++++++++++++++')

def wordPrint(dict1, key, list1):
    if key in dict1.keys():
        value = dict1[key]
        if '|' in value:
            list = []
            for v_i in value:
                if v_i != '|':
                    list.append(v_i)
            key = random.choice(list)
            if key != 'null':
                wordPrint(dict1, key, list1)
            else:
                pass
        else:
            for s_i in value:
                key = s_i
                wordPrint(dict1, key, list1)
    else:
        list1.append(key)
        return list1


if __name__ == '__main__':
    generate()

