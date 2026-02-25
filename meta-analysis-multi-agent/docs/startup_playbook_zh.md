# 启动手册（中文）——现有问题与论文写作起步

> 目标：从“只有模板”快速进入“可产出初稿”的执行状态。

## 一、现有版本的主要问题（为什么你会觉得不够用）

1. **模板完整，但缺“第一周可执行动作”**
   - 之前的内容强调结构化与规范性，但没有把“今天先做什么、明天做什么”写成可执行任务。
2. **写作入口不够前置**
   - 仅提供了 `docs/manuscript.md` 骨架，缺少“如何把统计结果映射成段落”的写作步骤。
3. **缺少可直接复制的运行清单**
   - 有 SOP，但没有“开工 checklist + 角色分工 + 日常节奏”一页式指南。
4. **交付标准偏抽象**
   - 有 done_definition，但缺少“每个阶段最少要交什么文件才算通过”。

## 二、建议的起步方式（0 到初稿）

## Step 0：确定论文目标（30–60 分钟）
- 在 `templates/project_charter.md` 填好：
  - 研究问题（PICO/PECO）
  - 主要结局（primary outcome）
  - 效应量类型（OR/RR/HR/MD/SMD）
- 输出：冻结研究范围，不再随意改题。

## Step 1：冻结 protocol（半天）
- 填写 `templates/protocol.md`。
- 同步维护 `templates/eligibility_criteria.yaml`，确保机器可读。
- 输出：纳排标准、亚组分析、敏感性分析预先定义。

## Step 2：搭建任务板（30 分钟）
- 用 `templates/status_board.csv` 创建你的真实任务：
  - T-001 方案定稿
  - T-002 检索式
  - T-003 去重
  - T-004 提取
  - T-005 统计
  - T-006 初稿
- 输出：每个任务有 owner、截止日期、依赖关系。

## Step 3：并行推进证据与写作（第 1–2 周）
- Search Agent 完成检索和筛选日志。
- Stats Agent 产出主分析结果表（先最小可用结果）。
- Writing Agent **从 Methods 和 Results 先写**，不要等 Discussion。
- 输出：`docs/manuscript.md` 中至少形成可审稿的 Methods + Results。

## Step 4：质量门禁（提交前）
- 对照 `workflows/sop.md` 的 Gate A–E。
- 检查数字一致性：正文数字是否都能追溯到分析表。
- 输出：PRISMA checklist 初版 + 一次完整内审。

---

## 三、论文写作的推荐顺序（高效版本）

1. **Methods（先写）**：最稳定、最不依赖“结果解释”。
2. **Results（次写）**：完全基于统计产物，禁止手写数字。
3. **Introduction（再写）**：以研究空白和临床意义收束。
4. **Discussion（最后写）**：解释异质性、局限性、外部效度。
5. **Abstract（最后最后写）**：避免前后不一致。

---

## 四、首周执行清单（可直接照做）

- [ ] 完成 `project_charter.md`
- [ ] 完成 `protocol.md`
- [ ] 完成 `eligibility_criteria.yaml`
- [ ] 初始化 `status_board.csv` 并指定负责人
- [ ] 完成首轮数据库检索并记录查询语句
- [ ] 形成初版筛选日志（含排除理由）
- [ ] 建立 `docs/manuscript.md` 的 Methods 草稿

完成以上 7 项后，项目就已从“模板阶段”进入“生产阶段”。

