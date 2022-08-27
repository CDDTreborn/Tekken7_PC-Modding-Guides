import bpy

# TK7 Bone Organizer
# In OBJECT mode, select Armature
# Run Script
# Primary bones will be on layer 16 and Finger bones on layer 17
# Works best on fresh TK7 Armature. To reset make sure all layeres are selected
# and change bone layer to 0.  

bpy.context.object.data.bones['Spine1'].layers[0] = False
bpy.context.object.data.bones['Spine1'].layers[16] = True
bpy.context.object.data.bones['Spine2'].layers[0] = False
bpy.context.object.data.bones['Spine2'].layers[16] = True
bpy.context.object.data.bones['Neck'].layers[0] = False
bpy.context.object.data.bones['Neck'].layers[16] = True
bpy.context.object.data.bones['Head'].layers[0] = False
bpy.context.object.data.bones['Head'].layers[16] = True
bpy.context.object.data.bones['Hip'].layers[0] = False
bpy.context.object.data.bones['Hip'].layers[16] = True
bpy.context.object.data.bones['L_Pinky1'].layers[0] = False
bpy.context.object.data.bones['L_Pinky1'].layers[17] = True
bpy.context.object.data.bones['L_Pinky2'].layers[0] = False
bpy.context.object.data.bones['L_Pinky2'].layers[17] = True
bpy.context.object.data.bones['L_Pinky3'].layers[0] = False
bpy.context.object.data.bones['L_Pinky3'].layers[17] = True
bpy.context.object.data.bones['L_Ring1'].layers[0] = False
bpy.context.object.data.bones['L_Ring1'].layers[17] = True
bpy.context.object.data.bones['L_Ring2'].layers[0] = False
bpy.context.object.data.bones['L_Ring2'].layers[17] = True
bpy.context.object.data.bones['L_Ring3'].layers[0] = False
bpy.context.object.data.bones['L_Ring3'].layers[17] = True
bpy.context.object.data.bones['L_Middle1'].layers[0] = False
bpy.context.object.data.bones['L_Middle1'].layers[17] = True
bpy.context.object.data.bones['L_Middle2'].layers[0] = False
bpy.context.object.data.bones['L_Middle2'].layers[17] = True
bpy.context.object.data.bones['L_Middle3'].layers[0] = False
bpy.context.object.data.bones['L_Middle3'].layers[17] = True
bpy.context.object.data.bones['L_Index1'].layers[0] = False
bpy.context.object.data.bones['L_Index1'].layers[17] = True
bpy.context.object.data.bones['L_Index2'].layers[0] = False
bpy.context.object.data.bones['L_Index2'].layers[17] = True
bpy.context.object.data.bones['L_Index3'].layers[0] = False
bpy.context.object.data.bones['L_Index3'].layers[17] = True
bpy.context.object.data.bones['L_Thumb1'].layers[0] = False
bpy.context.object.data.bones['L_Thumb1'].layers[17] = True
bpy.context.object.data.bones['L_Thumb2'].layers[0] = False
bpy.context.object.data.bones['L_Thumb2'].layers[17] = True
bpy.context.object.data.bones['L_Thumb3'].layers[0] = False
bpy.context.object.data.bones['L_Thumb3'].layers[17] = True
bpy.context.object.data.bones['R_Pinky1'].layers[0] = False
bpy.context.object.data.bones['R_Pinky1'].layers[17] = True
bpy.context.object.data.bones['R_Pinky2'].layers[0] = False
bpy.context.object.data.bones['R_Pinky2'].layers[17] = True
bpy.context.object.data.bones['R_Pinky3'].layers[0] = False
bpy.context.object.data.bones['R_Pinky3'].layers[17] = True
bpy.context.object.data.bones['R_Ring1'].layers[0] = False
bpy.context.object.data.bones['R_Ring1'].layers[17] = True
bpy.context.object.data.bones['R_Ring2'].layers[0] = False
bpy.context.object.data.bones['R_Ring2'].layers[17] = True
bpy.context.object.data.bones['R_Ring3'].layers[0] = False
bpy.context.object.data.bones['R_Ring3'].layers[17] = True
bpy.context.object.data.bones['R_Middle1'].layers[0] = False
bpy.context.object.data.bones['R_Middle1'].layers[17] = True
bpy.context.object.data.bones['R_Middle2'].layers[0] = False
bpy.context.object.data.bones['R_Middle2'].layers[17] = True
bpy.context.object.data.bones['R_Middle3'].layers[0] = False
bpy.context.object.data.bones['R_Middle3'].layers[17] = True
bpy.context.object.data.bones['R_Index1'].layers[0] = False
bpy.context.object.data.bones['R_Index1'].layers[17] = True
bpy.context.object.data.bones['R_Index2'].layers[0] = False
bpy.context.object.data.bones['R_Index2'].layers[17] = True
bpy.context.object.data.bones['R_Index3'].layers[0] = False
bpy.context.object.data.bones['R_Index3'].layers[17] = True
bpy.context.object.data.bones['R_Thumb1'].layers[0] = False
bpy.context.object.data.bones['R_Thumb1'].layers[17] = True
bpy.context.object.data.bones['R_Thumb2'].layers[0] = False
bpy.context.object.data.bones['R_Thumb2'].layers[17] = True
bpy.context.object.data.bones['R_Thumb3'].layers[0] = False
bpy.context.object.data.bones['R_Thumb3'].layers[17] = True
bpy.context.object.data.bones['L_Shoulder'].layers[0] = False
bpy.context.object.data.bones['L_Shoulder'].layers[16] = True
bpy.context.object.data.bones['L_Arm'].layers[0] = False
bpy.context.object.data.bones['L_Arm'].layers[16] = True
bpy.context.object.data.bones['L_ForeArm'].layers[0] = False
bpy.context.object.data.bones['L_ForeArm'].layers[16] = True
bpy.context.object.data.bones['L_Hand'].layers[0] = False
bpy.context.object.data.bones['L_Hand'].layers[16] = True
bpy.context.object.data.bones['L_UpLeg'].layers[0] = False
bpy.context.object.data.bones['L_UpLeg'].layers[16] = True
bpy.context.object.data.bones['L_Leg'].layers[0] = False
bpy.context.object.data.bones['L_Leg'].layers[16] = True
bpy.context.object.data.bones['L_Foot'].layers[0] = False
bpy.context.object.data.bones['L_Foot'].layers[16] = True
bpy.context.object.data.bones['L_Toe'].layers[0] = False
bpy.context.object.data.bones['L_Toe'].layers[16] = True
bpy.context.object.data.bones['R_Shoulder'].layers[0] = False
bpy.context.object.data.bones['R_Shoulder'].layers[16] = True
bpy.context.object.data.bones['R_Arm'].layers[0] = False
bpy.context.object.data.bones['R_Arm'].layers[16] = True
bpy.context.object.data.bones['R_ForeArm'].layers[0] = False
bpy.context.object.data.bones['R_ForeArm'].layers[16] = True
bpy.context.object.data.bones['R_Hand'].layers[0] = False
bpy.context.object.data.bones['R_Hand'].layers[16] = True
bpy.context.object.data.bones['R_UpLeg'].layers[0] = False
bpy.context.object.data.bones['R_UpLeg'].layers[16] = True
bpy.context.object.data.bones['R_Leg'].layers[0] = False
bpy.context.object.data.bones['R_Leg'].layers[16] = True
bpy.context.object.data.bones['R_Foot'].layers[0] = False
bpy.context.object.data.bones['R_Foot'].layers[16] = True
bpy.context.object.data.bones['R_Toe'].layers[0] = False
bpy.context.object.data.bones['R_Toe'].layers[16] = True
