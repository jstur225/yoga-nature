# 通用形态语法与体式签名

先描述形态，再寻找自然物。不要在签名阶段写花、树、海浪等语义名称。

## 1. 选择主表达方式

只选一个主方式，可记录一个次方式：

- **骨架型 skeleton**：辨识度来自肢体分支和连接关系。常见拓扑：I、V、Y、T、X、放射、多级分叉。
- **轮廓型 contour**：辨识度来自外轮廓曲线。常见拓扑：拱、U、S、波浪、螺旋、开环、闭环。
- **体块型 mass**：辨识度来自整体面积和重心。常见拓扑：三角、圆/椭圆、穹顶、团块、层叠、带孔体块。

判断问题：把人物缩成黑影后，最先被看见的是“枝杈”“曲线”还是“体块”？

再做一次显著性检查：把画面缩小并轻微模糊，仍然明显的关系才属于主结构。手指、掌形、面部、衣纹、被躯干遮挡的手臂和只靠体式知识才能辨认的细节一律降为 `secondary` 或 `ignore`，不得进入生图硬约束。

## 2. 方向与显著性

- 只描述第一眼可见的整体方向，不为人体节点建立坐标，也不记录肢体长度比例。
- 可用时钟或普通方向词记录主轴，例如“接近 12 点方向”“从左下趋向右上”；不要叠加角度、长度和节点误差预算。
- 另行记录 `flow_direction`：主轮廓、凝视或动势从哪一侧趋向哪一侧；螺旋和回卷可记录顺时针/逆时针。
- 方向敏感姿态记录 `handedness`：left-facing / right-facing / neutral。它只用于发现镜像错误，不代表自然对象必须复制人体朝向。
- 手指、头发、衣角、接触点和被遮挡的肢体不算主结构。

## 3. 三种主表达方式

### 骨架型

- `topology`：只记录粗粒度的 I / V / Y / T / X / radial / branched-chain。
- `dominant_axis`：一条决定第一眼的主轴。
- `major_turn_or_branch`：至多一个主要转向或分叉趋势；没有则省略。
- `center_of_mass`：整体重心偏上、偏下、偏左、偏右或居中。
- `primary_negative_space`：只有确实主导第一眼时才记录一个。

### 轮廓型

- `open_closed`：开放 / 闭合。
- `closure_type`：`intrinsic` 固有闭合 / `contact` 接触闭合 / `perceptual` 视觉闭合。
- `curve_family`：arc / U / S / wave / spiral / loop。
- `dominant_turn`：只记录一个主要回转方向。
- `curvature`：柔和、紧、均匀或突然折转；不记录精确端点。
- `center_of_mass`：整体重心位置。

闭合类型决定自然候选的约束强度：

- `intrinsic`：主体自身连续结构稳定围成孔洞，孔洞数量属于硬拓扑。
- `contact`：手脚、肢体或两段轮廓因接触/重叠暂时闭合。自然候选可用端点接近的开放弧或近环呼应，不强制真实接触。
- `perceptual`：观者通过缺口补全形状。只要求回转方向和主要负空间，不要求闭合。

不要把 `contact` 或 `perceptual` 升格为实体圆环；否则容易逼迫柔性自然物形成不可能的造型。

### 体块型

- `mass_family`：triangle / oval / dome / compact / layered / hollow。
- `aspect_tendency`：偏高、偏宽或紧凑，不记录精确比例。
- `center_of_mass`：重心位置。
- `symmetry`：对称 / 近对称 / 不对称，只作生成后观察。
- `primary_hole`：只有主导第一眼时才记录一个内部负空间。

## 4. 动作气质

选择一个主气质，可附一个次气质：

- `expansive-light`：舒展轻盈，长线条打开，视觉重量轻。
- `soft-flowing`：柔软流动，连续曲线，像水、风或藤蔓。
- `strong-grounded`：力量稳定，负重明显，角度硬朗，底座扎实。
- `inward-quiet`：内收安静，折叠、对称或保护性姿态。
- `twisted-coiled`：扭转聚拢，螺旋、交叠或围绕中心。

高难度不等于力量型。根据画面表现判断，不根据体式难度判断。

### 状态句与意象母题

形态签名完成后，再用一句不含自然物名称的短句回答：**这个身体正在经历什么？**

- 描述处境或张力，不描述体式难度，也不写“禅意、生命、自由”等空泛主题。
- 优先使用两个同时成立、彼此略有张力的状态，例如“失衡中的安静”“暴露中的信任”“收拢但仍留有缝隙”。
- 状态句只帮助选择候选，不进入成品，也不要求每张图都承担强象征。没有可靠共鸣时，宁可保持安静的结构呼应。

候选关系分三条平行通道：

- `form` 形：骨架、轮廓、重心和负空间相近。
- `force` 势：受力方向、动作节奏和时间阶段相近。
- `meaning` 意：两者处在相似的处境，让意义能由观者自行发现。

`form`、`force`、`meaning` 不互相依赖。自然候选先通过原生自然与非拟人化门槛，之后只需一条通道成立：可以形似，可以共享受力，也可以共享可观察的处境。`meaning` 不补偿人为塑形，但可以在完全没有几何对应时独立成为交付理由。

`meaning` 通道必须同时满足：

1. 同一个具体动词或状态句能描述人物和自然，例如收拢、承重、跃出、悬停、扎根、等待、沉降、展开；
2. 自然对象的行为从画面可见，不依赖“自由、生命、禅意、力量、重生、平静”等万能抽象词；
3. 遮住解释后，画面的节奏、处境或时间瞬间仍能被感到，而不是任意漂亮自然图。

## 5. 布局判定

记人体包围盒高宽比为 `R`。满足任一条件则使用左右布局：

1. `R ≥ 1.30`，且主轴与垂直方向夹角不超过 25°；
2. 连续主线跨越画面高度 70% 以上，且垂直跨度至少为水平跨度的 1.25 倍；
3. 倒立或单腿上伸在上下半幅中会被迫缩到容器高度的 70% 以下。

否则使用上下布局。边界情况以“不裁关键端点且人物占比更大”为准。

## 6. 宏观呼应门槛

### 所有模式

- 先按 nature-lookup.md 通过原生自然与非拟人化门槛，再比较姿态关系。
- 每个最终候选标记一种主关联通道：`form`、`force` 或 `meaning`；不同候选可以使用不同通道。
- 生成提示词最多携带两个 `primary` 宏观关系；其余关系只用于生成后比较。
- `form` 候选至少保留一个选定的宏观关系，但不要求节点、射线、孔洞或人体部位逐项相等；`force` 和 `meaning` 候选不要求几何关系。
- 只有当主要负空间被选为 `form` 通道的主关系时，固有闭合或主要负空间才作为硬关系；接触闭合和视觉闭合永远不要求实体闭环。

### 骨架型

- 可呼应一条主轴、一个主要分叉方向或一个不对称重心，通常只选其中一到两项。
- 次级分枝数量、节点数量和末端方向允许不同；不得把每条肢体翻译成一根枝、根、角、茎或浪线。
- 若候选只有在多个自然部件分别承担头、手臂、躯干和腿时才成立，判定失败。

### 轮廓型

- 可呼应一个主要回转方向、一段连续弧线或一个主要内向空间。
- 转向次数、端点位置和局部曲率允许自然偏差；不得把人体接触闭合翻译成规则圆环。
- 方向可以通过合成前水平翻转统一，但不得为统一方向扭曲对象。

### 体块型

- 可呼应整体高宽关系、重心、疏密或一个主要孔洞。
- 主体块数量和局部对称性无需相等；环境尺度和自然形成证据比几何精度优先。

宏观关系应足以在并置后被感知，但不能精确到像描摹人体。若相似度必须依赖角度、长度和节点的多项精确误差预算，说明候选过度拟合，应改用受力、重心或更含蓄的自然家族。

## 7. 输出模板

```yaml
pose_name: <名称或未知>
primary_mode: skeleton | contour | mass
secondary_mode: <可选>
topology: <Y / arc / triangle ...>
information_layers:
  primary: <最多两个宏观关系>
  secondary: <只用于生成后比较>
  ignore: <不得进入提示词的局部信息>
channel_signatures:
  form: <最多两个宏观形态、重心或负空间关系>
  force: <具体动词、受力方向和时间阶段>
  meaning: <不含自然物名称、可由画面观察的处境>
dominant_axis_or_turn: <一个整体方向或主要回转>
primary_negative_space: <可选；仅在主导第一眼时记录>
energy_primary: <动作气质>
energy_secondary: <可选>
material_tendency: light | medium | heavy | fluid
state_line: <不含自然物名称的身体状态句>
force_direction: <主要受力、趋向或回转方向>
flow_direction: <left-to-right / right-to-left / clockwise / counterclockwise / neutral>
handedness: left-facing | right-facing | neutral
temporal_moment: still | about-to-move | moving | settling
layout: side-by-side | top-bottom
layout_reason: <一句话>
```

## 8. 异类示例：轮式后弯

```yaml
pose_name: 轮式
primary_mode: contour
secondary_mode: mass
topology: open-arc
information_layers:
  primary: 连续开放拱线；重心低且两端承重
  secondary: 近对称；拱下留有大型开放空间
  ignore: 手掌接触、脚掌接触、面部和衣纹
channel_signatures:
  form: 连续开放拱线；拱下一个主要开放空间
  force: 从两端承重并向最高点撑开
  meaning: 身体暴露在外，同时把内部空间托起
dominant_axis_or_turn: 从左接地点向上回转后落向右侧
primary_negative_space: 拱线下方的大型开放空间
energy_primary: strong-grounded
energy_secondary: expansive-light
material_tendency: medium
state_line: 暴露在外，同时把内部空间托起
force_direction: 两端向下承重，中部向上撑开
flow_direction: left-to-right
handedness: neutral
temporal_moment: still
layout: top-bottom
layout_reason: 主轮廓横向展开，上下半幅能保留完整拱线
```

## 9. 骨架引导图 JSON

引导图是高风险例外，不是骨架型姿态的默认产物。只有候选自然对象本来就具有稳定、非拟人的刚性结构，文本生成连续失败，且用户已同意素材流向时才可使用。站立类姿态、植物分枝、树根以及任何可能被读成人体骨架的候选禁止使用。

引导图最多表达一个主轴和一个宏观转向，不画完整人体骨架。坐标均为人体包围盒内的归一化坐标：

```json
{
  "canvas": {"width": 1024, "height": 1536},
  "nodes": [{"id": "J1", "point": [0.50, 0.55]}],
  "strokes": [
    {"id": "A", "points": [[0.50, 0.10], [0.50, 0.90]], "weight": 18},
    {"id": "B", "points": [[0.50, 0.55], [0.78, 0.38]], "weight": 14}
  ],
  "closed_shapes": []
}
```

上例只是 JSON 格式演示，不对应任何固定体式。实际使用时只画批准保留的一到两个宏观关系，不画人体外形、完整肢体、面部或服装。用 `scripts/render_shape_guide.py` 转成非身份化参考图。
