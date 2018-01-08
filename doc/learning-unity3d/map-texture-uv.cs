using UnityEngine;
using System.Collections;

[ExecuteInEditMode]
public class CustomUVS : MonoBehaviour {
    public Vector2 topPoint;
    public Vector2 bottomPoint;
    public Vector2 leftPoint;
    public Vector2 rightPoint;
    public Vector2 frontPoint;
    public Vector2 backPoint;

    private Mesh m_mesh;
    public enum CubeFaceType
    {
        Top,
        Bottom,
        Left,
        Right,
        Front,
        Back
    };

    // Use this for initialization
    void Start () {
        MeshFilter meshFilter = GetComponent<MeshFilter>();
        if (meshFilter == null) {
            Debug.LogError("Script needs MeshFilter component");
            return;
        }

#if UNITY_EDITOR
        Mesh meshCopy = Mesh.Instantiate(meshFilter.sharedMesh) as Mesh;    // Make a deep copy
        meshCopy.name = "Cube";
        m_mesh = meshFilter.mesh = meshCopy;                                // Assign the copy to the meshes
#else
        m_mesh = meshFilter.mesh;
#endif
        if (m_mesh == null || m_mesh.uv.Length != 24) {
            Debug.LogError("Script needs to be attached to built-in cube");
            return;
        }

        UpdateMeshUVS();
    }

    // Update is called once per frame
    void Update () 
    {
#if UNITY_EDITOR
        UpdateMeshUVS();
#endif
    }

    void UpdateMeshUVS()
    {
        Vector2[] uvs = m_mesh.uv;
        // Front
        SetFaceTexture(CubeFaceType.Front, uvs);
        // Top
        SetFaceTexture(CubeFaceType.Top, uvs);
        // Back
        SetFaceTexture(CubeFaceType.Back, uvs);
        // Bottom
        SetFaceTexture(CubeFaceType.Bottom, uvs);
        // Left
        SetFaceTexture(CubeFaceType.Left, uvs);  
        // Right        
        SetFaceTexture(CubeFaceType.Right, uvs);   
        m_mesh.uv = uvs;
    }

    Vector2[] GetUVS(float originX, float originY)
    {
        Vector2[] uvs = new Vector2[4];
        uvs[0] = new Vector2(originX / 3.0f, originY / 3.0f);
        uvs[1] = new Vector2((originX + 1) / 3.0f, originY / 3.0f);
        uvs[2] = new Vector2(originX / 3.0f, (originY + 1) / 3.0f);
        uvs[3] = new Vector2((originX + 1) / 3.0f, (originY + 1) / 3.0f);
        return uvs;
    }

    void SetFaceTexture(CubeFaceType faceType, Vector2[] uvs)
    {
        if (faceType == CubeFaceType.Front) {
            Vector2[] newUVS = GetUVS(frontPoint.x, frontPoint.y);
            uvs[0]  = newUVS[0]; 
            uvs[1]  = newUVS[1];
            uvs[2]  = newUVS[2];
            uvs[3]  = newUVS[3];
        }else if (faceType == CubeFaceType.Back) {
            Vector2[] newUVS = GetUVS(backPoint.x, backPoint.y);
            uvs[10] = newUVS[0]; 
            uvs[11] = newUVS[1]; 
            uvs[6]  = newUVS[2]; 
            uvs[7]  = newUVS[3]; 
        }else if (faceType == CubeFaceType.Top) {
            Vector2[] newUVS = GetUVS(topPoint.x, topPoint.y);
            uvs[8] = newUVS[0]; 
            uvs[9] = newUVS[1]; 
            uvs[4]  = newUVS[2]; 
            uvs[5]  = newUVS[3]; 
        }else if (faceType == CubeFaceType.Bottom) {
            Vector2[] newUVS = GetUVS(bottomPoint.x, bottomPoint.y);
            uvs[12] = newUVS[0]; 
            uvs[14] = newUVS[1]; 
            uvs[15]  = newUVS[2]; 
            uvs[13]  = newUVS[3]; 
        }else if (faceType == CubeFaceType.Left) {
            Vector2[] newUVS = GetUVS(leftPoint.x, leftPoint.y);
            uvs[16] = newUVS[0]; 
            uvs[18] = newUVS[1]; 
            uvs[19]  = newUVS[2]; 
            uvs[17]  = newUVS[3]; 
        }else if (faceType == CubeFaceType.Right) {
            Vector2[] newUVS = GetUVS(rightPoint.x, rightPoint.y);
            uvs[20] = newUVS[0]; 
            uvs[22] = newUVS[1]; 
            uvs[23]  = newUVS[2]; 
            uvs[21]  = newUVS[3]; 
        }
    }
}
