from django.db import models
import functions
# Create your models here.
import config

class EncodingFormat(models.Model):
    """
        each function is a class with
           encode
           decode
        methods
    """
    FUNCTIONS = (
                    ('md5','pVault_MD5'),
                    ('salted_md5','pVault_Salted_MD5'),                    
                    ('ntlm','pVault_NTLM'),
                )
    
    id_tab   = models.AutoField(primary_key=True)
    name     = models.CharField(max_length=12, blank=False, null=False)
    function = models.CharField(choices=FUNCTIONS, max_length=33, blank=False, null=False)
    example  = models.CharField(max_length=128, blank=True, null=True, help_text="codes a 'hello!' string")
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Encoding formats"        
    
    def save(self, *args, **kwargs):
        if not self.example:
            enc_method = [i[1] for i in self.FUNCTIONS if i[0] == self.function][0]
            self.example = functions.__dict__[enc_method](functions._example_string)
        super(EncodingFormat, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return '%s %s' % (self.name, self.function)

class PasswordEncoding(models.Model):
    id_tab           = models.AutoField(primary_key=True)
    date_creation    = models.DateTimeField(auto_now=True)
    encoding         = models.ForeignKey(EncodingFormat)
    iv               = models.CharField(max_length=256, null=True,blank=True)
    secret           = models.CharField(max_length=256, null=True,blank=True)
    salt             = models.CharField(max_length=256, null=True,blank=True)
    is_active        = models.BooleanField()
    class Meta:
        #ordering = ['name']
        verbose_name_plural = "Password Encoding"        
    def __unicode__(self):
        return '%s' % (self.encoding)


class Server(models.Model):
    id_tab              = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=135, blank=False, null=False)
    date_creation       = models.DateTimeField(auto_now=True)
    description         = models.TextField(max_length=512, null=True,blank=True)
    is_active           = models.BooleanField()
    ip                  = models.CharField('hostname', max_length=46, blank=False, null=False)
    worker_queue        = models.CharField(max_length=46, null=True,blank=True, \
                          help_text="the running worker on the server listens to this queue, if needed")
    password_encoding   = models.ForeignKey(PasswordEncoding)
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Servers"        
    def __unicode__(self):
        return '%s' % self.name

class PasswordVault(models.Model):
    id_tab           = models.AutoField(primary_key=True)
    date_creation    = models.DateTimeField(auto_now=True)
    username         = models.CharField(max_length=135, blank=False, null=False)        
    password         = models.CharField(max_length=1024, null=False,blank=False, help_text="this will be filled with encrypted password encoded as hexlified string")
    description      = models.CharField(max_length=135, null=True,blank=True)    
    export_to_servers   = models.ManyToManyField(Server, null=True,blank=True)
    is_active           = models.BooleanField()    
    exported_to_servers = models.BooleanField()    
    class Meta:
        ordering = ['username']
        verbose_name_plural = "Password Vault (users credentials)"      
    
    def servers(self):
        s = '<ul>'
        for i in self.export_to_servers.all():
            s += '<li>%s</li>' % i.name
        s += '</ul>'
        return s
    servers.allow_tags = True # allows HTML and/or entities (e.g., &nbsp;)
    servers.short_description = 'on servers' # customize heading title in changelist
    servers.admin_order_field = 'on_servers' # a DB field to order in relation to

    def save(self, *args, **kwargs):
        super(PasswordVault, self).save(*args, **kwargs)

        if not self.pk:
            self.password = functions.pVault_encode_AES(config.secret, self.password, config.iv)
            # put it in history changelog            
            h = PasswordVaultHistory.objects.create(password_vault=self, value=self.password)
            self.passwordvaulthistory_set.add( h )
            
        else:
            # test if password is good
            try:
                functions.pVault_decode_AES(config.secret, self.password, config.iv)
            # if it changed, then crypt it again :)
            except:
                self.password =  functions.pVault_encode_AES(config.secret, self.password, config.iv)
                # put it in history changelog
                h = PasswordVaultHistory.objects.create(password_vault=self, value=self.password)
                self.passwordvaulthistory_set.add( h )
                
        super(PasswordVault, self).save(*args, **kwargs)
        
        # risalvo tutti gli exports
        for i in self.passwordvaultexports_set.filter(is_active=True):
            i.save()

    def __unicode__(self):
        return '%s' % (self.username)      
        #return '%s on %s' % (self.username, ','.join(self.on_servers) )

class PasswordVaultHistory(models.Model):
    id_tab           = models.AutoField(primary_key=True)
    password_vault   = models.ForeignKey(PasswordVault)
    date             = models.DateTimeField(auto_now=True)
    value            = models.CharField(max_length=256, null=True,blank=True)
    class Meta:
        #ordering = ['name']
        verbose_name_plural = "Password Vault history"        
    
    def __unicode__(self):
        return '%s %s' % (self.password_vault, self.date)

class PasswordVaultExports(models.Model):
    id_tab           = models.AutoField(primary_key=True)
    password_vault   = models.ForeignKey(PasswordVault)
    password_encoding  = models.ForeignKey(PasswordEncoding)
    value            = models.CharField(max_length=256, null=True,blank=True)
    is_active        = models.BooleanField()
    class Meta:
        #ordering = ['name']
        verbose_name_plural = "Password Vault exports"        
    
    def save(self, *args, **kwargs):
        psw        = functions.pVault_decode_AES(config.secret, self.password_vault.password, config.iv)
        enc_method = [i[1] for i in EncodingFormat.FUNCTIONS if i[0] == self.password_encoding.encoding.function][0]
        self.value =  functions.__dict__[enc_method](psw)
        super(PasswordVaultExports, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return '%s %s' % (self.password_encoding.encoding, self.password_vault)

