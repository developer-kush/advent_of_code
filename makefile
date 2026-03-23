
# Defaults
YEAR := $(shell date +%Y)
DAY := $(shell date +%d)

# Override defaults based on arguments
ARGS := $(MAKECMDGOALS)
ifneq ($(word 1, $(ARGS)),)
	DAY := $(word 1, $(ARGS))
endif
ifneq ($(word 2, $(ARGS)),)
	YEAR := $(word 1, $(ARGS))
	DAY := $(word 2, $(ARGS))
endif

# Ensure DAY is 0-padded (e.g. 5 -> 05)
DAY := $(shell printf "%02d" $(DAY))

.PHONY: run
run:
	@echo "$(GREEN)Running $(YEAR) Day $(DAY)$(RESET)"
	@cp input/$(YEAR)/$(DAY).input _in.txt
	@python3 $(YEAR)/$(DAY).py < input/$(YEAR)/$(DAY).input
	@rm _in.txt

# Catch-all rule to allow arguments to be treated as targets without error
%: run
	@:
