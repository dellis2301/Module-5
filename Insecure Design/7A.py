@app.route('/reset-password', methods=['POST'])
def reset_password():
    token = request.form['token']
    new_password = request.form['new_password']

    user = verify_reset_token(token)
    if not user:
        return 'Invalid token', 400

    user.password = hash_password(new_password)
    db.session.commit()
    return 'Password reset successful'
