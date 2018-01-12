
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

  
