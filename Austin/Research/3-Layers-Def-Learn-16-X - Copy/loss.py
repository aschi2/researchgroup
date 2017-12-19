import tensorflow as tf

def custom_loss(y_pred,y_true):
    left = tf.matmul(y_true,tf.transpose(tf.log(y_pred)))
    one_minus_y = tf.subtract(tf.ones_like(y_true),y_true)
    right = tf.matmul( one_minus_y, tf.transpose(y_pred))
    loss = tf.subtract(left,right)
    absloss = tf.abs(loss)
    return tf.reduce_mean(absloss)



def custom_loss_2(y_pred,y_true):
    # Value for this constant
    HARD_LEN_ZEROS = 10000
    left = tf.matmul(y_true,tf.transpose(tf.log(y_pred)))
    one_minus_y = tf.subtract(tf.ones_like(y_true),y_true)
    right_1 = tf.matmul( one_minus_y, tf.transpose(y_pred))
    # a 0-D Scaler tensor wth value 1/num-zeros see HARD_LEN_ZEROS
    numzero = tf.constant(1/HARD_LEN_ZEROS)
    right = tf.scalar_mul(numzero,right_1)  
    loss = tf.subtract(left,right) 
    squared_loss = tf.square(loss)
    return tf.reduce_mean(squared_loss)
    