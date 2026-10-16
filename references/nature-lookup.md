# 开放式自然候选搜索与评分

不要维护“体式 → 物种”的固定映射表。使用人物分层后的形、势、意签名，跨自然家族搜索候选。目标是含蓄押韵，不是寻找人体替身；形、势、意是三条平行的交付通道。

## 1. 候选覆盖

每轮初筛默认 6 个候选，覆盖至少 3 个家族，并从 `form / force / meaning` 各提出两个。某条通道确实找不到通过预审的候选时，记录失败原因并把名额转给另外两条通道；不得因为形候选容易想到，就省略势或意的搜索。

- 植物：花、叶、草、藤、树、根、种荚、蕨类。
- 水与天气：浪、水流、瀑布、漩涡、云、雨、冰、闪电。
- 地貌：山脊、洞穴、沙丘、岩层、河道、海岸。
- 动物：鸟、鱼、鹿角、贝壳、珊瑚、昆虫翅、动物姿态。
- 其他有机形态：菌类、骨骼、蜂巢、果实、种子。

这些只是搜索入口，不是允许清单。可以提出库外候选。

对于站立、平衡、Y/V/X 等容易被分枝对象拟人化的姿态，至少一半候选来自非分枝类家族。树、裸根、鹿角、珊瑚和分叉花茎不永久禁用，但默认标记为 `anthropomorphic_risk: high`，除非只使用其中一个宏观关系且单独观看完全不像人体。

## 2. 初筛与候选映射卡

初筛阶段只写一行，避免在明显不合格的候选上消耗长提示词：

```yaml
- candidate: <候选>
  native_form: <为何会自然出现>
  shape_behavior: stable | transient
  match_channel: form | force | meaning
  shared_relation: <宏观关系、具体动词或具体状态句>
  direction: <方向/手性>
  state_fit: <与状态句的关系>
  anthropomorphic_risk: low | medium | high
  synthetic_shape_risk: low | medium | high
  main_risk: <强行塑形/标本感/人体替身/概念海报/环境尺度/灰阶分离等>
```

只有综合排名前两位需要写完整候选卡：

每个候选必须写清楚为什么自然成立以及保留哪些宏观关系，不能只说“看起来像”：

```yaml
candidate: <自然候选>
family: <自然家族>
shape_behavior: stable | transient
primary_mode: skeleton | contour | mass
match_channel: form | force | meaning
primary_relations:
  - <form 时写宏观关系，最多两项；force/meaning 可为空>
shared_verb: <force/meaning 使用的可观察动词>
shared_state: <meaning 使用的具体状态句>
observable_natural_behavior: <画面中直接可见的自然行为>
causal_chain:
  cause: <风、重力、地形、生长或动物发力等成因>
  process: <正在发生的破碎、坠落、展开、起飞等过程>
  residue: <泡沫、飞沫、湿痕、雾气、扰动、遮挡等余波或痕迹>
capture_conditions: <可信的视点、快门表现、景深、天气和光线>
secondary_observations: <只用于生成后比较，不进入提示词>
ignored_pose_details: <不得映射的手指、隐藏肢体等>
native_form_basis: <该形态为何会在真实环境中自然出现>
required_coincidences: <为了像人体而要求的精确数量、笔直、平行、对称或等距条件>
staging_risk: low | medium | high
anthropomorphic_risk: low | medium | high
synthetic_shape_risk: low | medium | high
human_roles_visible: <能否被读成头/手臂/躯干/腿；列出或写 none>
energy_fit: pass | fail
material_fit: pass | fail
force_fit: <共同受力方向与动作节奏>
meaning_fit: <是否与状态句形成含蓄共鸣；不得只写抽象象征词>
temporal_moment: <自然对象正处于什么真实行为瞬间>
cliche_risk: low | medium | high
photo_feasibility: high | medium | low
```

`form` 候选卡最多保留两个宏观关系，不补全映射。`force` 和 `meaning` 可以没有几何对应，但必须写出共享动词、具体状态和可观察的自然行为。若需要三个以上独立自然部件承担人体角色，或只有靠多项精确巧合才能成立，应淘汰而不是继续补约束词。

## 3. 硬门槛

按以下顺序检查，任一失败都不得进入评分：

1. **原生形态门槛**：候选结构必须是该自然物常见或可信的生长、受力、流动状态；不仅要“生物学上可能”，还要在画面中像自然发生。若必须摆拍、挑出恰好数量、排齐、精确描线、镜像对称、形成规则圆环或违背物理规律才能匹配，直接淘汰。
2. **现场因果门槛**：正在流动、破碎、坠落、飞散、起飞或变形的候选，必须能写出并在画面中验证 `成因 → 过程 → 余波`。至少三项现场证据应相互支持；只有主体轮廓、没有浪组与泡沫、上游与湿痕、接触与扰动等因果痕迹，直接淘汰。
3. **摄影偶然性门槛**：必须像在有限视点、光线、快门和景深条件下拍到的现场，而不是为一个轮廓搭建的概念海报。全画面均匀锐化、无来由的发光边缘、过度居中、完美孤立主体、所有杂讯都服务同一形状或互相矛盾的运动模糊，直接淘汰。
4. **非拟人化门槛**：候选不得首先被读成人、人体骨架或自然物在摆动作。能迅速指出头、手臂、躯干、腿中的三个以上角色，或需要三个以上自然部件分别承担人体部位，直接淘汰。
5. **摄影可实现门槛**：必须能在一张未经拼贴或超现实变形的真实照片中清楚呈现，并带有环境尺度、部分遮挡、局部差异和不服务于目标形态的现场残留。
6. **通道关系门槛**：以下三条至少一条成立：
   - `form`：至少一个宏观轮廓、体块、重心或负空间关系清楚成立；
   - `force`：同一个具体动词、受力方向或时间阶段能自然描述人物与自然；
   - `meaning`：同一句具体状态句能描述两者，且自然行为在画面中直接可见，不靠万能抽象词或说明文字硬解释。
7. **光影表达门槛**：缩小后阴影、高光、雾气不得比自然物本体更先被读到，也不得靠阴影伪造姿态轮廓。
8. **气质冲突门槛**：明显相反的动势或材质直接淘汰，例如轻盈舒展配厚重岩块。

## 4. 评分

只给通过全部硬门槛的候选评分：

- 原生形态与现场因果可信度：35 分。
- 摄影偶然性、拍摄条件与环境证据：20 分。
- 非拟人化、低摆拍与低概念海报风险：15 分。
- 当前通道的关联质量：15 分。
- 可观察行为、时间阶段与状态清晰度：10 分。
- 构图与黑白灰阶适配：5 分。

评分总计 100 分，只用于排序，不阻断交付。候选必须通过全部硬门槛和至少一条通道关系门槛。分数相近时，优先更普通、更自然、更不需要解释的候选，而不是形状最像人体的候选。`form` 失败时继续使用 `force` 或 `meaning`；整批候选因自然性失败时重建候选池，最终使用 `meaning-led` 保障通道完成交付。

## 5. 跨类别示例

以开放拱形轮廓为例：

- 弯曲树干：若一条连续主干构成完整拱线，轮廓可能通过。
- 卷浪：若浪壁形成单一开放弧且转向次数一致，可能通过。
- 海蚀洞：若洞口是一个主要开放拱而非多孔体块，可能通过。
- 天鹅颈：曲线可能相似，但若主体还出现翅膀、腿等强结构，需要重新判断主表达方式。
- 三叉树枝：即使其中一段弯曲方向合适，也因容易被读成人体分支而属于高风险候选；只有单独观看完全自然且不承担多个人体角色时才可能通过。

任何类别都不是永久允许或永久禁用。候选是否合格只由本次签名决定。

### `meaning` 通道的边界示例

这些例子说明关系如何成立，不构成固定配对表：

- 深度折叠与缩入壳中的蜗牛可以共享“向内收拢、重心贴近地面、以外层保护内部”；不要求壳的螺旋复制人体骨架。
- 身体向上打开或短暂离开支撑面，与跃出水面、尚未落下的海豚可以共享“突破界面、上升、短暂悬停”；不能只用“自由”解释。
- 从稳定支点向外展开的姿态，与正在自然开放的花可以共享“从一点获得支撑并逐步展开”；不得把花瓣逐片解释成四肢。

同一对象不能因此适配所有体式。每次仍须写出本图可直接看到的动词、受力方向或时间瞬间；如果遮住解释后只剩下“漂亮、治愈、生命力”，则 `meaning` 不成立。

## 6. 生图提示词模板

先判断候选的 `shape_behavior`：

- `stable`：岩层、贝壳、叶片、成熟植物主体或动物身体等相对稳定对象。可以使用一个软宏观关系；只有其原生结构确实稳定时，才允许一个硬结构条件。
- `transient`：海浪、瀑布、水流、喷溅、云、雾、烟、火焰等瞬时或高可塑介质。硬几何预算为零；形态只能作为生成后的筛选结果。

### 稳定对象模板

```text
Scene: A real <natural subject> in its native environment.
Shared relation: <form: one macro relation; force: one concrete action/force; meaning: one observable state>.
Moment: <one observable action or transitional moment, without explaining symbolism>.
Natural behavior: believable gravity, growth or flow, with organic variation and environmental evidence.
Capture: documentary nature photograph from a plausible viewpoint, with coherent depth of field, exposure and local detail; when subject and surroundings share similar material, let the focal plane and texture scale establish a natural visual hierarchy.
Composition: <panel ratio and orientation>; subject scale appropriate to its family, with enough context and partial overlap to show scale; the primary mass or relation remains readable without becoming an isolated specimen.
Light and tones: natural light, preserved atmosphere, midtones and shadow detail; use believable local tonal or height separation when needed, never forced studio-like separation.
Avoid: anthropomorphic silhouette, body-part-like branches or roots, posed or sculpted growth, concept-poster composition, subject and surroundings sharing uniform density, gray value and sharpness, artificial outline or rim glow, uniform hyper-sharpness, <3–6 task-specific risks>, text, watermark, collage or CGI.
```

### 瞬时介质模板

```text
Scene: A documentary black-and-white photograph of <natural event> in <native setting>.
Cause and process: <real force or terrain> is causing <observable action> at <transitional moment>.
Field evidence: <at least three mutually supporting traces: surrounding wave sets, old foam, cross-chop, source channel, wetness gradients, spray, mist, impact disturbance, partial occlusion>.
Capture: <credible shore/cliff/ground-level viewpoint>; <fast or slow shutter appropriate to every moving element>; natural depth, haze and uneven local sharpness.
Composition: the event occupies roughly 35–65% of the frame, slightly off-center when plausible, with enough surrounding environment to explain it.
Avoid: target body shape, perfect arc or vertical ribbon, isolated hero subject, sculptural silhouette, symmetrical poster framing, luminous edges, HDR/dehaze look, uniform micro-detail, CGI, text or watermark.
```

海浪应用时写“受离岸风影响、正在自然破碎的一组涌浪”，并要求相邻浪组、交叉细浪、旧泡沫和方向一致的飞沫；不要写“单一优雅长弧”或要求整条浪峰为体式让路。

瀑布应用时写“雨后水流沿不规则岩层下降”，并要求可见或可推断的上游入口、撞击分流、湿润梯度、底部飞雾与回水；不要写“修长中央竖线”“发光丝带”或清空两侧环境来突出轮廓。

常规提示词控制在约 100–160 个英文词。`force` 和 `meaning` 提示词不描述人体形状，只描述自然对象真实发生的动作或处境。详细的人体对应关系、评分过程和哲学解释不进入提示词；它们用于选择候选和验收结果。

哲学意味来自对象的真实行为与画面关系，不来自抽象形容词。不要用 `spiritual / zen / symbolic / profound / freedom / life` 等词要求模型“制造意义”；改写成可观察的瞬间，例如“起飞前仍有一只脚承重”“浪峰将落未落”“枝条受风弯曲但没有折断”。优先选择介于两种状态之间的未完成瞬间，但不得为此摆拍、拟人化或违反自然规律。

### 几何约束预算

- `stable` 提示词最多保留一个硬结构条件和一个软关系条件，其余用“主要、接近、略微、整体重心、疏密关系”等词表达。
- `transient` 提示词不得出现目标弧线、竖线、人体方向、负空间或干净剪影。用“受离岸风影响的破碎浪组”“雨后沿不规则岩层下降的瀑布”等自然事件类型保留可能的关系，生成后再筛选实际形态。
- 不要叠加 `exactly`、`perfectly straight`、`parallel`、`equally spaced`、`one on each side`、`centered`、`symmetrical`。当三个以上这类条件同时出现时，先回到候选阶段判断是否选错自然物。
- 即使对象刚性稳定，也不要求与人体相同的节点数。植物、树根、海草、藤蔓、云、浪等有机或柔性对象只控制整体动势，不精确指定每根元素的位置。
- 环境不是装饰：保留邻近植被、风、水、地表、遮挡和景深证据。主体可以清楚，但不能像从环境里抠出后单独陈列。

只有候选属于稳定、非拟人的刚性结构，文本生成连续失败，并且用户已同意所说明的生成服务与素材流向时，才可提供只含一个主轴和一个宏观转向的 `shape-guide.png`。站立类姿态、植物分枝和树根不得使用引导图。

```text
Image 1 is a geometry-only guide. Use only its dominant axis and one broad directional change. Do not match every node or stroke, and do not form a human-like silhouette.
```

柔性但相对稳定的自然物可以写“整体回卷、一个主要内向空间”等软关系。云、浪、瀑布、喷溅等瞬时介质不得直接写目标曲线；禁止要求任何柔性对象精确闭合成规则圆环。

## 7. 生成后双重验收

两个阶段严格按顺序执行。第一阶段不得查看人体图、形态签名或候选解释。

### 第一阶段：只看自然性

1. 单独看是否像未经摆拍的真实自然状态；“某物种确实可能长得很直”不足以通过，整幅画面仍不能呈现刻意挑选、排齐或对称陈列的感觉。
2. 正常尺寸下，成因、过程和余波是否连续；水流、飞沫、雾气、湿痕、接触扰动和邻近环境是否相互支持。
3. 快门凝固或拖影、景深、空气透视、锐度和视点是否自洽；是否出现重复纹理、均匀微细节、发光丝带或拼接式边界；当主体与环境材质相近时，主要体块是否仍能靠自然的高度、疏密、局部灰阶或景深差异被读出。
4. 是否有不服务于目标形态的真实现场残留，还是所有元素都像为了一个轮廓而设计。
5. 是否首先让人想到人体、骨架、戒指、Logo、支架、植物标本、产品陈列或概念海报。
6. 是否能迅速指出头、手臂、躯干、腿中的三个以上角色。
7. 阴影边界是否压过主体轮廓，或替自然物伪造了人体形状。

现场因果或拍摄条件不自洽，或第 5、6 项为“是”，即失败，不得进入第二阶段。先以正常尺寸检查局部连续性，再缩至 64px 检查整体读取；缩略图不能替代正常尺寸的摄影真实性检查。

### 第二阶段：按通道检查含蓄呼应

1. 把通过第一阶段的自然图缩小到 64px，记录第一眼的形态、动作和处境。
2. `form`：选定的一到两个宏观关系是否仍能被感知，但没有变成人体替身。
3. `force`：同一个具体动词、受力方向或时间阶段是否能直接描述两幅图。
4. `meaning`：同一句具体状态句是否能描述两者，自然行为是否在画面中可见，而不是依赖抽象象征词或长篇解释。
5. 当前候选只需对应通道通过；动作气质、环境尺度、灰阶分离和摄影风格仍须协调。

盲检问题：遮住人物参考图后，这张自然照片是否仍像自然摄影师偶然遇到并拍下的画面？若首先让人想到戒指、Logo、支架、植物标本、产品陈列，或明显能逐项指出“这根是手、那根是腿”，判定失败。

每个候选从零独立生成 1–2 个版本，不连续编辑失败图。两个版本都失败时换候选或通道；候选池耗尽时进入 `meaning-led` 保障通道，使用普通、自然、行为清楚的真实瞬间完成交付。只有宿主生图能力缺失或持续技术失败时，才退回提示词交付并说明技术限制。
