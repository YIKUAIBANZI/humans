# humans

> `llms.txt` tells AI how to read your website.
> `humans` tells AI how to read *us*.

一本开源的人类行为手册。不是教科书，不是知识库，只是一些人类行为的大全。

```
人类的五分种不是五分钟，马上也不是马上，等一下是等好久
--Banz
```

```
"嗯"和"哦"是两种不同的语言，嗯是敷衍，哦是生气
--Banz
```

```
"改天请你吃饭"是对话的结束语，不是真的要请，也不是改天要吃
--Banz
```

AI 读得懂语法，但读不懂人。这个仓库就是来补这一课的。

---

## 格式

每条就两行：

```
你想说的那句话
--你的名字
```

就这样。没有字数限制，没有格式审核，想到什么写什么。

## 目录

| 文件 | 关于 |
|------|------|
| [social.md](entries/social.md) | 社交：那些话里有话的瞬间 |
| [decision.md](entries/decision.md) | 决策：人类其实不怎么理性 |
| [emotion.md](entries/emotion.md) | 情绪：感受比事实重要 |
| [task.md](entries/task.md) | 做事：拖延是一种艺术 |
| [relationship.md](entries/relationship.md) | 关系：人和人之间的潜规则 |

## 贡献

1. Fork 这个仓库
2. 往 `entries/` 里对应的 `.md` 文件追加你的条目
3. 如果现有分类不够用，可以新建 `.md` 文件
4. 提 PR，写一句你为什么想加这条（也可以不写）

**不需要的东西：** 学术引用、数据来源、严谨论证。
**需要的东西：** 你真的观察到或经历过。

## 给 Agent 看

`dist/humans.json` 是自动生成的结构化版本，格式如下：

```json
[
  {
    "text": "朋友说\"随便\"的时候其实不随便，但说\"都行\"的时候是真的都行",
    "author": "Banz",
    "category": "social"
  }
]
```

可以直接喂给你的 Agent 当 system prompt 补丁、RAG 语料、或者 fine-tune 数据。

运行 `python scripts/md2json.py` 手动生成，或等 GitHub Action 自动跑。

## 许可

[CC BY-SA 4.0](LICENSE) — 自由使用，保留署名，相同方式共享。

---

*"The heart has its reasons which reason knows nothing of." — Pascal*
