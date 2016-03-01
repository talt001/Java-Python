import java.awt.Color;

class Proj05Runner extends Proj05{

	  public Proj05Runner(){//constructor
	    System.out.println("Charles Combs.");
	  }//end constructor
	  //----------------------------------------------------//

	  public void run(){

	    Picture skater = new Picture("Proj05a.bmp");
	    skater.explore();
	    skater = crop(skater,6,59,392,293);

	    Picture hole = new Picture("Proj05b.bmp");
	    hole.explore();
	    hole = crop(hole,6,59,392,293);


	    Picture snowScene = new Picture("Proj05c.jpg");
	    snowScene.explore();
	    snowScene = crop(snowScene,6,59,392,293);

	    //Make all the pixels darker in the snow scene except
	    // for those in the location of the hole. Make them
	    // brighter.
	    darkenBackground(hole,snowScene);

	    //Apply a red tint to the skater
	    redTint(skater);

	    //Draw the skater on the snowScene.
	    greenScreenDraw(skater,snowScene,0,0);

	    //Display students name on the final output and
	    // display it.
	    snowScene.addMessage("Charles Combs.",10,15);

	    snowScene.explore();
	    System.out.println(snowScene);

	  }//end run method
	  //----------------------------------------------------//

	  //Assumes the source has a pure green background.
	  // Applies a red tint to every pixel that is not pure
	  // green.
	  private void redTint(Picture pic){
	    Pixel[] pixels = pic.getPixels();
	    Color color = null;
	    int red = 0;
	    int green = 0;
	    int blue = 0;
	    for(int cnt = 0;cnt < pixels.length;cnt++){
	      color = pixels[cnt].getColor();
	      //Apply a red tint to all non-green pixels
	      if(!(color.equals(Color.GREEN))){
	        //Increase the value of the red component
	        red = color.getRed();
	        if(red*1.25 < 255){
	          red = (int)(red * 1.25);
	        }else{
	          red = 255;
	        }//end else
	        //Decrease the value of blue and green
	        green = (int)(color.getGreen()*0.8);
	        blue = (int)(color.getBlue()*0.8);

	        //Apply the new color to the pixel.
	        pixels[cnt].setColor(new Color(red,green,blue));
	      }//end if
	    }//end for loop
	  }//end redTint
	  //----------------------------------------------------//

	  //Assumes the pattern image has a pure green background.
	  // Assumes that the pattern and the destination have the
	  // same dimensions. Darkens every pixel in the
	  // destination that is at the location of a green pixel
	  // in the pattern. Applies a red tint to every pixel
	  // in the destination that is at the location of a
	  // non-green pixel in the pattern
	  private void darkenBackground(
	                           Picture pattern,
	                           Picture dest){

	    Pixel[] patternPixels = pattern.getPixels();
	    Pixel[] destPixels = dest.getPixels();
	    Color color = null;
	    int red = 0;
	    int green = 0;
	    int blue = 0;

	    for(int cnt = 0;cnt < patternPixels.length;cnt++){
	      color = patternPixels[cnt].getColor();
	      if(color.equals(Color.GREEN)){
	        //Darken corresponding pixel in the destination.
	        color = destPixels[cnt].getColor();
	        destPixels[cnt].setColor(color.darker());
	      }else{
	        //Apply a red tint to the corresponding pixel in
	        // the destination.
	        color = destPixels[cnt].getColor();
	        red = color.getRed();
	        if(red*1.25 < 255){
	          red = (int)(red * 1.25);
	        }else{
	          red = 255;
	        }//end else
	        green = (int)(color.getGreen() * 0.8);
	        blue = (int)(color.getBlue() * 0.8);
	        destPixels[cnt].setColor(new Color(red,green,blue));
	      }//end else
	    }//end for loop
	  }//end darkenBackground
	  //----------------------------------------------------//

	  //Assumes a source image with a pure green background.
	  // Copies all non-green pixels from the source image to
	  // the destination image at the location explained
	  // below. Note that JPEG images typically won't have
	  // a pure green background even if they had a pure
	  // green background before being compressed into the
	  // JPEG format.  BMP images work well for this.
	  private void greenScreenDraw(
	                           Picture source,
	                           Picture dest,
	                           //Place the upper-left corner
	                           // of the source image at the
	                           // following location in the
	                           // destination image.
	                           int destX,
	                           int destY){
	    int width = source.getWidth();
	    int height = source.getHeight();
	    Pixel pixel = null;
	    Color color = null;

	    for(int row = 0;row < height;row++){
	      for(int col = 0;col < width;col++){
	        color = source.getPixel(col,row).getColor();
	        if(!(color.equals(Color.GREEN))){
	          pixel = dest.getPixel(destX + col,destY + row);
	          pixel.setColor(color);
	        }//end if
	      }//end inner loop
	    }//end outer loop

	  }//end greenScreenDraw
	  //----------------------------------------------------//

	  //Crops a Picture object to the given width and height
	  // with the upper-left corner located at startCol and
	  // startRow.
	  private Picture crop(Picture pic,int startCol,
	                                   int startRow,
	                                   int width,
	                                   int height){
	    Picture output = new Picture(width,height);

	    int colOut = 0;
	    int rowOut = 0;
	    int col = 0;
	    int row = 0;
	    Pixel pixel = null;
	    Color color = null;
	    for(col = startCol;col < startCol+width;col++){
	      for(row = startRow;row < startRow+height;row++){
	        color = pic.getPixel(col,row).getColor();
	        pixel = output.getPixel(colOut,rowOut);
	        pixel.setColor(color);
	        rowOut++;
	      }//end inner loop
	      rowOut = 0;
	      colOut++;
	    }//end outer loop
	    return output;
	  }//end crop

	}//end class Proj05Runner
