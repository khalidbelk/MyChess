##
## MyChess
## Makefile
## File description:
## Makefile
##

SRC		:=	src/main.py

NAME	:=	mychess

all: $(NAME)

$(NAME):
	@echo "\033[1;32m[$(NAME)]\033[0m"
	@echo "Compiling $(SRC)..."
	@echo "#!/usr/bin/env python3" > $(NAME)
	@cat $(SRC) >> $(NAME)
	@chmod +x $(NAME)
	@echo "\033[1;32m✓ Done\033[0m"

clean:
	@echo "\033[1;31m[Clean]\033[0m"
	rm -f $(NAME)

fclean: clean
	@rm -f $(NAME)

re: fclean all

.PHONY: all $(NAME) clean fclean re
