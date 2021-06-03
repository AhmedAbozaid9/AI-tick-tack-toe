

            if(event.type == pygame.MOUSEBUTTONDOWN and isPlayerTurn):
                mouseX = event.pos[0] 
                mouseY = event.pos[1]
                #add player input
                idx = mapCords.getIdx(mouseX,mouseY)