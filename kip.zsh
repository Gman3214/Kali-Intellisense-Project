fpath=(~/.kip/Completions $fpath)

for file in ~/.kip/Functions/*; do
    [ -r "$file" ] && [ -f "$file" ] && source "$file"
done
