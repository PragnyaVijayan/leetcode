def find_number_rooms_with_ocean_view(room_height):
    
    rooms_with_ocean_view = []
    max_height = -10000
    
    for i in range(len(room_height) - 1, -1 ,-1):
        if room_height[i] > max_height:
            rooms_with_ocean_view.append(i)
            max_height = room_height[i]
            
    print(rooms_with_ocean_view)
    print(len(rooms_with_ocean_view))
    
def main():
    room_heights = [4, 4, 4, 4, 4]
    
    find_number_rooms_with_ocean_view(room_heights)
    
if __name__ == '__main__':
    main()
