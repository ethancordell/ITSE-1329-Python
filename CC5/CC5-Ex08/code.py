def first_last6(nums):
  if nums[:1] == 6:
    return 'True'
  elif nums[2:] == 6:
    return 'True'
  else:
    return 'False'
