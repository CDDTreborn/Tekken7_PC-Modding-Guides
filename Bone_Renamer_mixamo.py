import bpy

def rename_bones():
    
    dict = {
        'mixamorig:Hips': 'Hip',
        'mixamorig:Spine': 'Spine1', 
        'mixamorig:Spine1': 'Spine2', 
        'mixamorig:Spine2': 'Spine2.001', 
        'mixamorig:Neck': 'Neck', 
        'mixamorig:Head': 'Head', 
        'mixamorig:HeadTop_End': 'ATH_Head_Top', 
        'mixamorig:LeftShoulder': 'L_Shoulder', 
        'mixamorig:LeftArm': 'L_Arm', 
        'mixamorig:LeftForeArm': 'L_ForeArm', 
        'mixamorig:LeftHand': 'L_Hand', 
        'mixamorig:LeftHandThumb1': 'L_Thumb1', 
        'mixamorig:LeftHandThumb2': 'L_Thumb2', 
        'mixamorig:LeftHandThumb3': 'L_Thumb3', 
        'mixamorig:LeftHandThumb4': 'L_Thumb4_null', 
        'mixamorig:LeftHandIndex1': 'L_Index1', 
        'mixamorig:LeftHandIndex2': 'L_Index2', 
        'mixamorig:LeftHandIndex3': 'L_Index3', 
        'mixamorig:LeftHandIndex4': 'L_Index4_null', 
        'mixamorig:LeftHandMiddle1': 'L_Middle1', 
        'mixamorig:LeftHandMiddle2': 'L_Middle2', 
        'mixamorig:LeftHandMiddle3': 'L_Middle3', 
        'mixamorig:LeftHandMiddle4': 'L_Middle4_null', 
        'mixamorig:LeftHandRing1': 'L_Ring1', 
        'mixamorig:LeftHandRing2': 'L_Ring2', 
        'mixamorig:LeftHandRing3': 'L_Ring3', 
        'mixamorig:LeftHandRing4': 'L_Ring4_null', 
        'mixamorig:LeftHandPinky1': 'L_Pinky1', 
        'mixamorig:LeftHandPinky2': 'L_Pinky2', 
        'mixamorig:LeftHandPinky3': 'L_Pinky3', 
        'mixamorig:LeftHandPinky4': 'L_Pinky4_null', 
        'mixamorig:RightShoulder': 'R_Shoulder', 
        'mixamorig:RightArm': 'R_Arm', 
        'mixamorig:RightForeArm': 'R_ForeArm', 
        'mixamorig:RightHand': 'R_Hand', 
        'mixamorig:RightHandThumb1': 'R_Thumb1', 
        'mixamorig:RightHandThumb2': 'R_Thumb2', 
        'mixamorig:RightHandThumb3': 'R_Thumb3', 
        'mixamorig:RightHandThumb4': 'R_Thumb4_null', 
        'mixamorig:RightHandIndex1': 'R_Index1', 
        'mixamorig:RightHandIndex2': 'R_Index2', 
        'mixamorig:RightHandIndex3': 'R_Index3', 
        'mixamorig:RightHandIndex4': 'R_Index4_null', 
        'mixamorig:RightHandMiddle1': 'R_Middle1', 
        'mixamorig:RightHandMiddle2': 'R_Middle2', 
        'mixamorig:RightHandMiddle3': 'R_Middle3', 
        'mixamorig:RightHandMiddle4': 'R_Middle4_null', 
        'mixamorig:RightHandRing1': 'R_Ring1', 
        'mixamorig:RightHandRing2': 'R_Ring2', 
        'mixamorig:RightHandRing3': 'R_Ring3', 
        'mixamorig:RightHandRing4': 'R_Ring4_null', 
        'mixamorig:RightHandPinky1': 'R_Pinky1', 
        'mixamorig:RightHandPinky2': 'R_Pinky2', 
        'mixamorig:RightHandPinky3': 'R_Pinky3', 
        'mixamorig:RightHandPinky4': 'R_Pinky4_null', 
        'mixamorig:LeftUpLeg': 'L_UpLeg', 
        'mixamorig:LeftLeg': 'L_Leg', 
        'mixamorig:LeftFoot': 'L_Foot', 
        'mixamorig:LeftToeBase': 'L_Toe', 
        'mixamorig:LeftToe_End': 'L_Toe1_null', 
        'mixamorig:RightUpLeg': 'R_UpLeg', 
        'mixamorig:RightLeg': 'R_Leg', 
        'mixamorig:RightFoot': 'R_Foot', 
        'mixamorig:RightToeBase': 'R_Toe', 
        'mixamorig:RightToe_End': 'R_Toe1_null'
 

    }
    
    for b in bpy.context.object.data.bones:
        if b.name in dict.keys():
            b.name = dict[b.name]

rename_bones()