echo ""
echo "comparing files"
cat res/message.txt; echo ""
cat res/guess.txt; echo ""
SIZE1=$(stat -f%z res/message.txt)
SIZE2=$(stat -f%z res/guess.txt)
DIFF1=$(cmp -l res/message.txt res/guess.txt | wc -l | sed 's/^ *//g')
DIFF2=$(expr $SIZE1 - $SIZE2)
RES=$(expr $DIFF1 + ${DIFF2#-})

echo "Character difference(s) = $DIFF1" 
echo "Size difference(s) = $DIFF2"
echo "number of error = $RES"
echo ""
