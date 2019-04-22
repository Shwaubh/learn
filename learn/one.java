class Box
{
  float width;
  float height;
  float depth;

public Box(float width, float height, float depth)
{
  this.height = height;
  this.depth  = depth;
  this.width  =  width;
}
public float getVolume()
{
  return width*height*depth;
}

}
class one
{
  public static void main(String[] args) {
    Box box = new Box(10.2f, 11.3f, 12.6f);
    System.out.print(box.getVolume());
  }
}
