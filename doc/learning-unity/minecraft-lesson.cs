
向左转（角速度） 
GetComponent<Rigidbody>().angularVelocity = new Vector3(0,-1f,0) 
angularVelocity ＝ （0,0,0)  停止旋转 

向前向后移动 
GetComponent<RigidBody>().velocity = new Vector3(0,0,20)
velocity = (0,0,0)  停止

loot - 
harvest - 
puff 

void OnMouseDown() 
void Update()
void Start()

实现steve 近身点击block消除的功能： 
  1. 摄像机添加 Collider, block上添加碰撞检测代码，在 OnTriggerEnter() 检测Camera碰撞允许点击Destroy

Partical 粒子显示block消失时的爆裂特效（puff）

Constant Force 常数力
- Force 常数恒力，不变的力
- Relative Force  在 Update()使用，连续的施加力

Update()刷新函数中设置速度
gameObject.transform.Translate(Vector3.forward*speed*Time.deltaTime)   deltaTime - 帧刷新之间的时间间隔

Raycast 射线检测 
  RaycastHit hit
  Physics.Raycast(origin,direction,out hit,length)    direction : 表示一个向量 , 可以由两个空间位置相减得到 , length : 向量的长度 Vector3.magnitude
